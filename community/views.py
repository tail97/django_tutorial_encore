from django.shortcuts import render
from .forms import Form, Article
# Create your views here.

def write(request):
    # if(request의 post true이면)
    # 사용자가 입력한 form 데이터를 변수에 저장하고
    # ORM으로 DB에 저장하기
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Form()
    # else
    form = Form()

    #return render(request, 'html템플릿 파일.html', data)
    return render(request, 'community/write.html', {'form':form})

def articleList(request):
    article_list = Article.objects.all()
    return render(request, 'community/list.html', {'article_list':article_list})

def viewDetail(request, num=1):
    # 클릭한 레코드를 DB 읽어오기
    article_detail = Article.objects.get(id=num)
    # article_detail = get_object_or404(Article, id=num)
    return render(request, 'community/view_detail.html', {'article_detail':article_detail})

def index(request):
    latest_article_list = Article.objects.all().order_by('-cdate')[:3]
    print(latest_article_list)
    return render(request, 'index.html', {'latest_article_list':latest_article_list})

from django.views.generic import CreateView, ListView, DetailView, UpdateView ,DeleteView
from community.models import Article
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import AccessMixin
from django_tutorial.views import OwnerOnlyMixin

class ArticleListView(ListView):
    model = Article
    template_name = 'community/list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name= 'community/view_detail.html'

class WriteFormView(LoginRequiredMixin,CreateView):
    model = Article
    fields = ['name', 'title', 'contents', 'url', 'email']
    template_name = 'community/write.html'
    success_url = reverse_lazy("community:list")

    def form_valid(self,form):
        return super().form_valid(form)

#변경(login user 자료만 list_up)
class ArticleChangeView(LoginRequiredMixin,ListView):
    template_name = "community/change_list.html"
    def get_queryset(self):
        return Article.objects.filter(owner=self.request.user)



# 로그인 user 메모 수정(Update) 
class ArticleUpdateView(OwnerOnlyMixin, UpdateView):
    model = Article
    template_name = 'community/article_update.html'
    fields = ['name', 'title', 'contents', 'url', 'email']
    success_url = reverse_lazy('community:change_list')

# 로그인 user 메모 삭제(Delete)
class ArticleDeleteView(OwnerOnlyMixin, DeleteView):
    model = Article
    template_name = 'community/article_delete.html'
    success_url = reverse_lazy('community:change_list')
