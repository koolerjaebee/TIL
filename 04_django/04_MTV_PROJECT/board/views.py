from django.shortcuts import render, redirect
from .models import Article


# Read
def index(request):  # 모든 게시글 목록을 보여주는 view
    articles = Article.objects.all()
    return render(request, 'board/index.html', {
        'articles': articles
    })


# Create
def new(request):  # 새로운 게시글을 작성할 html
    return render(request, 'board/new.html')


def create(request):  # 입력 데이터를 DB에 저장
    article = Article()
    article.title = request.GET.get('input_title')
    article.content = request.GET.get('input_content')
    article.save()
    return redirect(f'/board/articles/{article.id}')


def show(request, article_id):  # 특정 게시글을 보여주는 view(일)
    article = Article.objects.get(id=article_id)
    return render(request, 'board/show.html', {
        'article': article
    })


# Update
def edit(request):  # 특정 게시글을 수정할 화면을 주는 view(일)
    return render(request, 'board/edit.html')


# Delete
def delete(request, article_id):  # 특정 게시글을 삭제하는 view(일)
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('/board/articles')
