from django import forms
from .models import Article, Comment

# forms.Form => Data 입력/검증 + HTML 제공 => Model 정보 모름
# forms.ModelForm => Data 입력/검증 + HTML 제공 => Model 정보를 알고 있음


class ArticleForm(forms.Form):
    title = forms.CharField(min_length=2, max_length=100)
    content = forms.CharField()


# forms.Form => Data 입력 및 검증

class ArticleModelForm(forms.ModelForm):
    # 1. Data 입력 및 검증
    # 2. HTML 생성
    title = forms.CharField(min_length=2)

    class Meta:
        model = Article
        fields = '__all__'


class CommentModelForm(forms.ModelForm):
    content = forms.CharField(min_length=2, max_length=200)  # 200자를 검증

    class Meta:
        model = Comment
        fields = ('content',)

class ArticleForm(forms.Form):
    title = forms.CharField(
        min_length=2, max_length=100,
        widget=forms.Textarea(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter title plz',
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-class',
                'placeholder': 'Content is required',
                'rows': 5,
                
            }
        )
    )
