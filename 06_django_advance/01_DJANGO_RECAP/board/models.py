from django.db import models
from django.urls import reverse


class Article(models.Model):
    # id는 저절로 생성
    # null = False 기본값
    title = models.CharField(max_length=100)
    content = models.TextField()

    # method 추가는 migrate을 하지 않아도 된다. (동사의 특징, 명사의 추가는 migrate)
    def get_absolute_url(self):
        return reverse("board:detail", kwargs={"id": self.id})
