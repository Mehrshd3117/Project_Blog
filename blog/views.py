from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from blog.models import Article, Category, Comment, Message
from django.core.paginator import Paginator
from .forms import ContactUsForm, MessageForm
from django.views.generic.base import View, TemplateView, RedirectView
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView, ArchiveIndexView, YearArchiveView
from django.urls import reverse, reverse_lazy
from .mixins import CustomLoginRequiredMixin


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, "blog/article_detail.html", {'article': article})


def article_list(request):
    articles = Article.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 1)
    objects_list = paginator.get_page(page_number)
    return render(request, "blog/article_list.html", {'articles': objects_list})


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


def contactus(request):
    if request.method == 'POST':
        form = MessageForm(data=request.POST)
        if form.is_valid():
            instance = form.save(commit=True)
    else:
        form = MessageForm()
    return render(request, "blog/contact_us.html", {'form': form})


class HomePageRedirect(RedirectView):
    # url = "/articles/list"
    pattern_name = "blog:article_detail"
    permanent = False
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(*args, **kwargs)


class ArticleList(TemplateView):
    pass


class UserList(ListView):
    queryset = User.objects.all()
    template_name = "blog/user_list.html"


class ArticleDetailView(DetailView):
    model = Article


class ArticleListView(CustomLoginRequiredMixin, ListView):
    model = Article
    context_object_name = "articles"
    paginate_by = 1
    queryset = Article.objects.filter(published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "Mehrshad"
        return context


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


class MessagesListView(ListView):
    model = Message


class MessageUpdateView(UpdateView):
    model = Message
    fields = "__all__"
    template_name_suffix = '_update_form'
    success_url = reverse_lazy("home_app:home")


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy("home_app:home")

# class ArchiveIndexArticleView(ArchiveIndexView):
#     model = Article
#     date_field = "updated"
#
#
# class YearArchiveArticleView(YearArchiveView):
#     model = Article
#     date_field = "pud_date"
#     make_object_list = True
#     allow_future = True
#     template_name = "blog/article_archive_year.html"


class ArchiveIndexArticleView(ArchiveIndexView):
    model = Article
    date_field = "pub_date"


class YearArchiveArticleView(YearArchiveView):
    model = Article
    date_field = "pub_date"
    make_object_list = True
    allow_future = True



