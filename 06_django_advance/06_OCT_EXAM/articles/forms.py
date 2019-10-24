from django import forms

from .models import Article


# forms / models 앞은 복수형, Form / Model 은 단수형 & Capital
# forms.Form / models.Model
class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content',)  # title 과 content 만 검증(is_valid())한다.
