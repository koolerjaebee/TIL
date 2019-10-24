from django.shortcuts import render, redirect, get_object_or_404  # redirect && get_object_or_404
# decorators
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.decorators import login_required
# User Model 을 가져오는 함수
from django.contrib.auth import get_user_model

from .models import Article
from .forms import ArticleModelForm


def like(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    user = request.user
    # if user in article.like_users.all():
    if article.like_users.filter(id=user.id).exists():
        article.like_users.remove(user)
    else:
        article.like_users.add(user)
    return redirect('articles:article_list')


@require_GET
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/index.html', {
        'articles': articles,
    })


@require_GET
def article_detail(request, article_id):
    # get_object_or_404 의 1번 인자: 모델명, 2번인자: "id="
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'articles/detail.html', {
        'article': article,
    })


@login_required
@require_http_methods(['GET', 'POST'])
def article_create(request):
    if request.method == 'POST':
        form = ArticleModelForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            # article.user_id = requset.user.id
            article.save()
            return redirect('articles:article_detail', article.id)
    else:
        form = ArticleModelForm()
    return render(request, 'articles/form.html', {
        'form': form,
    })


@login_required
@require_http_methods(['GET', 'POST'])
def article_update(request, article_id):
    # create 에서 복붙 후 Update 추가사항
    # 0. article 하나 찾기
    article = get_object_or_404(Article, id=article_id)
    # 1. User 비교하기
    if article.user != request.user:
        return redirect('articles:article_list')
    if request.method == 'POST':
        # 2. instance 주기
        form = ArticleModelForm(request.POST, instance=article)
        if form.is_valid():
            # 3. 알아서 지우기
            form.save()
            return redirect('articles:article_detail', article.id)
    else:
        # 4. 또 instance 주기
        form = ArticleModelForm(instance=article)
    return render(request, 'articles/form.html', {
        'form': form,
    })


@login_required
@require_POST
def article_delete(request, article_id):
    # 주의! User 비교하기
    article = get_object_or_404(Article, id=article_id)
    if article.user == request.user:
        article.delete()
    return redirect('articles:article_list')
