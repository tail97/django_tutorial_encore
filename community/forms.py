from django.forms import ModelForm
from community.models import Article


class Form(ModelForm):
    class Meta:
        model = Article
        fields = ['name','title','content','url','email'] #내가 넣을 DB입력 정보