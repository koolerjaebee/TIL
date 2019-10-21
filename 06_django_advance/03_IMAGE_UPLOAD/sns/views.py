from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required

from .models import Posting, Comment
from .forms import PostingModelForm, CommentModelForm


@require_GET
def posting_list(request):
    postings = Posting.objects.all()
    return render(request, 'sns/posting_list.html', {
        'postings': postings,
    })


@login_required
@require_GET
def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comments = posting.comments.all()  # posting.comment_set 이 아닌 이유는 Model => related_name
    is_like = True if posting.like_users.filter(id=request.user.id).exists() else False
    return render(request, 'sns/posting_detail.html', {
        'posting': posting,
        'comments': comments,
        'is_like': is_like,
    })


@login_required
@require_POST
def create_posting(request):
    form = PostingModelForm(request.POST, request.FILES)  # 검증 & 저장 준비
    if form.is_valid():  # 검증!
        posting = form.save(commit=False)  # 저장 => Posting 객체 return
        posting.user = request.user  # anonymous? => 그럴리 없음
        posting.save()
        return redirect(posting)  # 성공하면 detail page
    else:
        return redirect('sns:posting_list')  # 실패하면 list page


@login_required
@require_POST
def delete_posting(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    if request.user == posting.user:
        posting.delete()
    return redirect('sns:posting_list')


@login_required
@require_POST
def create_comment(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    form = CommentModelForm(request.POST)  # content 만 값을 확인 
    if form.is_valid():  # content 만 값을 검증
        comment = form.save(commit=False)  # 아직 posting_id 가 비어있기 때문에, 저장하는 '척' 만 하고 Comment 객체 return
        comment.posting = posting  # comment.posting_id = posting.id
        comment.user = request.user
        comment.save()
    return redirect(posting)


@login_required
@require_POST
def delete_comment(request, posting_id, comment_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect(posting)


@login_required
@require_POST
def toggle_like(request, posting_id):
    user = request.user
    posting = get_object_or_404(Posting, id=posting_id)
    # user.like_postings.add(posting)  # 같은 의미
    # if user in posting.like_users.all():  # Python == 느림
    if posting.like_users.filter(id=user.id).exists():
        posting.like_users.remove(user)  # Delete
    else:
        posting.like_users.add(user)  # Create
    return redirect(posting)
