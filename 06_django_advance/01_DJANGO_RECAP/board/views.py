from django.shortcuts import render, redirect
from .models import Article


def index(request):
    return render(request, 'board/index.html')


def list(request):
    articles = Article.objects.all()  # [<A1>, <A2>, <A3>, ...]
    context = {'articles': articles}
    return render(request, 'board/list.html', context=context)


def detail(request, id):
    article = Article.objects.get(id=id)
    context = {'article': article}
    return render(request, 'board/detail.html', context=context)


def new(request):
    return render(request, 'board/new.html')


def create(request):
    article = Article()
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    context = {'article': article}
    return redirect(f'/board/articles/{article.id}')
