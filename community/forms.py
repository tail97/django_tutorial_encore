from django.forms import ModelForm
from .models import Article

class Form(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'title', 'contents', 'url', 'email']#내가 넣을 DB입력 정보