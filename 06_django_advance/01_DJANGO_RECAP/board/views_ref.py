from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import (require_GET, require_http_methods, require_POST)
from IPython import embed
​
from .forms import ArticleModelForm
from .models import Article
​
​
# CRUD
@require_http_methods(['GET', 'POST'])  # 비공식적으로 존재하는 요청이 있음. 얘네 말고 다른 요청이 들어올 수 있기 때문에
def new(request):
    # 요청이 GET/POST 인지 확인한다.
    # 만약 POST라면
    if request.method == 'POST':
        # ArticleModelForm을 생성하고 Data를 채운다(binding).
        form = ArticleModelForm(request.POST)
        # embed()  디버깅할 때만 써야하고 실제로 사용할 때는 꼭 지워야 함.
        # binding 된 form이 유효한지 체크한다.
        if form.is_valid():
            # 유효하다면 form을 저장한다.
            article = form.save()  # save는 리턴값이 있음.
            # 저장한 article detail로 redirect 한다.
            return redirect(article)  # model에 get_absolute_url을 넣어놨기 때문에 article만 써도 되는 것. redirect('board:detail', article.id)랑 같은 의미
        # form 이 유효하지 않다면,
        else:
            # 유효하지 않은 입력데이터를 담은 HTML과 에러메시지를 사용자한테 보여준다.
            return render(request, 'board/new.html', {
                'form': form,
            })
​
    # GET이라면
    else:
        # 비어있는 form(HTML 생성기)을 만든다.
        form = ArticleModelForm()
        # form과 html을 사용자에게 보여준다.
        return render(request, 'board/new.html', {
            'form':form,
        })
​
def list(request):
    articles = Article.objects.all()
    return render(request, 'board/list.html', {
        'articles': articles,
    })
​
def detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'board/detail.html', {
        'article': article,
    })
​
@require_http_methods(['GET', 'POST'])
def edit(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        form = ArticleModelForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect(article)
    else:
        form = ArticleModelForm(instance=article)  # 모델 폼에 article을 넣겠다.
    return render(request, 'board/edit.html', {
        'form': form,
    })
​
def delete(request):
    pass