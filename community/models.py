from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):#클래스를 만들어서 DB를 입력할 입력란을 구현
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    contents = models.TextField()
    url = models.URLField()
    email = models.EmailField()
    cdate = models.DateTimeField(auto_now_add=True)
    mdate = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

class Meta:
    verbose_name_plural = "아티클 작성하기"
    ordering = ('-mdate',)
    def __str__(self):
        return f"{self.title} -- {self.name} -- {self.cdate}"
    def get_absolute_url(self): # models에 포함된 메소드
        return reverse('community:view_detail', args=(self.id,))