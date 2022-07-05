from django.shortcuts import render, redirect
from blog.models import Article


def home(request):
    articles = Article.objects.all()
    recent_articles = Article.objects.all()
    return render(request, 'home/home.html', {'articles': articles, "name": "codeyad"})



def sidebar(request):
    data = {'name': 'Mehrshad'}
    return render(request, 'includes/sidebar.html', context=data)