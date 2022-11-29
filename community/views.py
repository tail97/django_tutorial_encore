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
    return render(request,'write.html', {'form':form} )


def articleList(request):
    article_list = Article.objects.all()
    return render(request,"list.html",{'article_list':article_list})

def viewDetail(request,num=1):
    # 클릭한 레코드를 db 읽어오기
    article_detail = Article.objects.get(id=num)
    return render(request,"view_detail.html", {'article_detail':article_detail})