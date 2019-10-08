from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST

from .models import Article
from .forms import ArticleModelForm


@require_GET
def index(request):
    return render(request, 'board/index.html')


@require_GET
def list(request):
    articles = Article.objects.all()  # [<A1>, <A2>, <A3>, ...]
    context = {'articles': articles}
    return render(request, 'board/list.html', context=context)


@require_GET
def detail(request, id):
    article = get_object_or_404(Article, id=id)
    context = {'article': article}
    return render(request, 'board/detail.html', context=context)


def new(request):
    if request.method == 'POST':
        form = ArticleModelForm(request.POST)

        if form.is_valid():
            article = form.save()

            return redirect(article)
    else:
        form = ArticleModelForm()

    return render(request, 'board/new.html', {
        'form': form,
    })


def edit(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect(article)
    else:
        context = {'article': article}
        return render(request, 'board/edit.html', context=context)


@require_POST
def delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('/board/articles/')
