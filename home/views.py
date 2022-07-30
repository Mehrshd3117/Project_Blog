from django.shortcuts import render, redirect
from blog.models import Article


def home(request):
    articles = Article.objects.all()
    return render(request, 'home/home.html', {'articles': articles})

