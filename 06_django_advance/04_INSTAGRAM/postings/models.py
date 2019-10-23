from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django_extensions.db.models import TimeStampedModel
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

User = get_user_model()

class HashTag(TimeStampedModel):  # TimeStampedModel은 created와 modified가 저절로 생김
    content = models.CharField(max_length=20, unique=True)

class Posting(TimeStampedModel):
    like_users = models.ManyToManyField(User, related_name='like_posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='postings')
    hashtags = models.ManyToManyField(HashTag, blank=True, related_name='postings')
    content = models.CharField(max_length=140)

    class Meta:
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse("postings:posting_detail", kwargs={"posting_id": self.pk})
    

class Image(models.Model):
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE, related_name='images')
    file = ProcessedImageField(
        processors=[ResizeToFit(600, 600, mat_color=(45,45,45))],  # 수정
        upload_to='postings/images',
        format='JPEG',
        options={'quality': 90},
    )

# p.image_set.all()  => related_name이 default값
# p.images.all()  => related_name='images'

class Comment(TimeStampedModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=140)

