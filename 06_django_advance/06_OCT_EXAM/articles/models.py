from django.db import models
from django.conf import settings  # 1. 만약 import 되어 있다면,
from django.contrib.auth import get_user_model # 2. 아무것도 import 안되어 있다면,
User = get_user_model()

class Article(models.Model):
    # ForeignKey, 두 번째 인자: on_delete=
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    # 내가 뭐라고 접근할지 = ... related_name = 남이 나를 뭐라고 부를지
    like_users = models.ManyToManyField(User, related_name='like_articles')
