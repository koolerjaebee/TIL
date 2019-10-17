from django.db import models
from django.urls import reverse


class Article(models.Model):
    # id는 저절로 생성
    # null = False 기본값
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # method 추가는 migrate을 하지 않아도 된다. (동사의 특징, 명사의 추가는 migrate)
    def get_absolute_url(self):
        return reverse("board:article_detail", kwargs={"article_id": self.id})


class Comment(models.Model):
    content = models.CharField(max_length=200)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
