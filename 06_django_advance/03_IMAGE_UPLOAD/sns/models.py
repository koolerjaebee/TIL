from django.db import models
from django.urls import reverse

"""
$ python manage.py migrate <APP_NAME> zero  => migration un-apply
$ rm <APP_NAME>/migrations/0*
"""

class Posting(models.Model):
    content = models.TextField()
    icon = models.CharField(max_length=30, default='')
    image = models.ImageField(blank=True)  # $ pip install pillow
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("sns:posting_detail", kwargs={"posting_id": self.pk})
    
    def __str__(self):
        return f'{self.pk}: {self.content[:20]}'
