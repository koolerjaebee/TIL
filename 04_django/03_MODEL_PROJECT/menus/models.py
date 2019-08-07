from django.db import models


class Menu(models.Model):
    # name : 메뉴이름 STRING
    # price : 가격 FLOAT
    # category : 카테고리 STRING
    # 모델링 => 견적 => 테이블 생성 => CRUD
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=50)
