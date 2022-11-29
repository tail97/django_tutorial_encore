from django.shortcuts import render
from .forms import Form

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
