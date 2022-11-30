from django.shortcuts import render
from .forms import Form
from .models import Article

# Create your views here.
def write(request):
    form = Form()
    
    # request의 post true이면
    #사용자가 입력한 form 데이터를 변수에 저장하고
    # orm으로 db에 저장 
    #아니면
    if request.method=='POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = Form()
    # return render(request,html템플릿파일.html,data)
    return render(request,'community/write.html', {'form':form} )# 3개의 파라미터가 들어간다


def articleList(request):
    article_list = Article.objects.all()
    return render(request,"community/list.html",{'article_list':article_list})# 3개의 파라미터가 들어간다

def viewDetail(request,num=1):
    # 클릭한 레코드를 db 읽어오기
    article_detail = Article.objects.get(id=num)
    return render(request,"community/view_detail.html", {'article_detail':article_detail})# 3개의 파라미터가 들어간다

def index(request):
    # -cdate는 내림차순, +cdate는 오름차순 
    latest_article_list = Article.objects.all().order_by('-cdate')[:3]
    print(latest_article_list) # 데이터를 잘 가지고 오는걸 확인하는 코드 
    return render(request,"index.html",{'latest_article_list':latest_article_list})# 3개의 파라미터가 들어간다