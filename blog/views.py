from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from blog.models import Article, Category, Comment, Message, Like
from django.core.paginator import Paginator
from .forms import ContactUsForm, MessageForm
from django.views.generic import ListView, DetailView, FormView, CreateView
from django.urls import reverse, reverse_lazy
from .mixins import CustomLoginRequiredMixin


def category_detail(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    articles = category.artilces.all()
    return render(request, "blog/article_list.html", {'articles': articles})


def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 1)
    objects_list = paginator.get_page(page_number)
    return render(request, "blog/article_list.html", {"articles": objects_list})


class ArticleDetailView(CustomLoginRequiredMixin, DetailView):
    model = Article

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article.objects.all(), slug=slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment'] = Comment.objects.all()
        context['form'] = Comment()
        #like
        if self.request.user.is_authenticated:
            if self.request.user.likes.filter(article__slug=self.object.slug, user_id=self.request.user.id).exists():
                context['is_liked'] = True
            else:
                context['is_liked'] = False

        return context


class ArticleListView(CustomLoginRequiredMixin, ListView):
    model = Article
    context_object_name = "articles"
    paginate_by = 1
    queryset = Article.objects.filter(published=True).order_by('-created', )


class ContactUsView(FormView):
    template_name = "blog/contact_us.html"
    form_class = MessageForm
    success_url = reverse_lazy("home_app:home")

    def form_valid(self, form):
        form_data = form.cleaned_data
        Message.objects.create(**form_data)
        return super().form_valid(form)


class MessageView(CreateView):
    model = Message
    fields = ('title', 'text', 'age', 'date')
    success_url = reverse_lazy("home_app:home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["messages"] = Message.objects.all()
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.email = self.request.user.email
        instance.save()
        return super().form_valid(form)

    def get_success_url(self):
        return super(MessageView, self).get_success_url()


def like(request, slug, pk):
    if request.user.is_authenticated:
        try:
            like = Like.objects.get(article__slug=slug, user_id=request.user.id)
            like.delete()
            return JsonResponse({"response": "unliked"})
        except:
            Like.objects.create(article_id=pk, user_id=request.user.id)
            return JsonResponse({"response": "liked"})

    return redirect("blog:article_detail", slug)
