from django import forms
from .models import Article

# forms.Form => Data 입력 및 검증


class ArticleModelForm(forms.ModelForm):
    # 1. Data 입력 및 검증
    # 2. HTML 생성
    title = forms.CharField(min_length=2)

    class Meta:
        model = Article
        fields = '__all__'
