from .models import Article
from django import forms
from martor.fields import MartorFormField

class NewArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['editor', 'pub_date']


# class NewArticleForm(forms.Form):
#     title = forms.CharField(label='title', max_length=30)
#     content = MartorFormField()
#     article_image = forms.ImageField()
    
    