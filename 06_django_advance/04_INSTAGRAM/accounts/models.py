from django.conf import settings
from django.urls import reverse
# User 는 AbstractUser를 상속받고 AbstractUser는 AbstractBaseUser를 상속받음
from django.contrib.auth.models import AbstractUser
from django.db import models
from faker import Faker

f = Faker()


class User(AbstractUser):  # 우리가 만든 User를 사용할 것이기 때문에 settings에 덮어씌워줘야 함
    fans = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='stars')
    # User 모델을 확장할지 안할지 모르겠을 때는 일단 만들어주고 추후에 필요시 확장하면 됨. 그럴 때 class User(AbstractUser): pass를 써두면 됨
    def __str__(self):
        return self.username

    @classmethod
    def dummy(cls, n):
        for i in range(n):
            u = cls()
            u.username = f.first_name()
            u.set_password('123456789')
            u.save()
    
    def get_absolute_url(self):
        return reverse("accounts:user_page", kwargs={"user_id": self.pk})
