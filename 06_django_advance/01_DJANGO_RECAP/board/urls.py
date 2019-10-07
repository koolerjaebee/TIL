from django.urls import path
from . import views


app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),  # board/ == board:index
    # Read 글 목록(list) render
    path('articles/', views.list, name='list'),
    # Read 글 상세(detail) render
    path('articles/<int:id>/', views.detail, name='detail'),

    # Create 글 쓰기(new) render
    path('articles/new/', views.new, name='new'),
    # Create 글 저장(create)
    path('articles/create/', views.create, name='create'),

    # Update 글 수정쓰기(edit) render
    path('articles/<int:id>/edit/', views.edit, name='edit'),
    # Update 글 실제수정(update)
    path('articles/<int:id>/update/', views.update, name='update'),

    # Delete 글 삭제(delete)
    path('articles/<int:id>/delete/', views.delete, name='delete'),
]
