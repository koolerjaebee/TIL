from django.conf import settings
from django.db import models
from django.urls import reverse
from faker import Faker

"""
$ python manage.py migrate <APP_NAME> zero
$ rm <APP_NAME>/migrations/0*
"""

f = Faker()

class Posting(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_postings', blank=True)
    content = models.TextField()
    icon = models.CharField(max_length=30, default='')
    image = models.ImageField(blank=True)  # $ pip install pillow
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at', ]   # created_at 을 descending 내림차순으로.

    def get_absolute_url(self):  # Detail 페이지를 쓸 거라면 만들어요.
        return reverse("sns:posting_detail", kwargs={"posting_id": self.pk})
    
    def __str__(self):
        return f'{self.pk}: {self.content[:20]}'

    @classmethod
    def dummy(cls, n):
        for _ in range(n):
            cls.objects.create(
                user_id=1,
                content=f.sentence(),
                icon='fas fa-angrycreative'
            )


class Comment(models.Model):
    # related_name 이 없으면, posting.comment_set / 아래아 같다면, posting.comments
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['created_at']
    
    @classmethod
    def dummy(cls, n, posting_id):
        for _ in range(n):
            cls.objects.create(
                user_id=1,
                posting_id=posting_id,
                content=f.sentence(),
            )
    
    def __str__(self):
        return f'{self.id}: {self.content[:10]}'
