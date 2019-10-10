from django.urls import path
from . import views


app_name = 'board'

urlpatterns = [
    # Read 글 목록(list) render
    path('articles/', views.article_list, name='article_list'),
    # Read 글 상세(detail) render
    path('articles/<int:article_id>/', views.article_detail, name='article_detail'),

    # Create 글 쓰기(new) render
    path('articles/new/', views.new_article, name='new_article'),
    # # Create 글 저장(create)
    # path('articles/create/', views.create, name='create'),
    # 합치면서 필요 없어짐

    # Update 글 수정쓰기(edit) render
    path('articles/<int:article_id>/edit/', views.edit_article, name='edit_article'),
    # # Update 글 실제수정(update)
    # path('articles/<int:id>/update/', views.update, name='update'),
    # 마찬가지로 리팩토링

    # Delete 글 삭제(delete)
    path('articles/<int:article_id>/delete/', views.delete_article, name='delete_article'),

    # Comment Create
    path('articles/<int:article_id>/comments/new', views.new_comment, name='new_comment'),

    path('articles/<int:article_id>/comments/<int:comment_id>/delete', views.delete_comment, name='delete_comment'),
]
