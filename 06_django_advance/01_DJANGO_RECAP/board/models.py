from django.db import models


class Article(models.Model):
    # id는 저절로 생성
    # null = False 기본값
    title = models.CharField(max_length=100)
    content = models.TextField()
