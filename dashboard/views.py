from django.shortcuts import render
from .models import CountryData
from .forms import CountryDataForm

# Create your views here.
def dashboard(request):
    # if request method == post
    #   valid하다면
    #   폼에 입력 데이터를 저장
    # else
    #   폼객체를 생성
    #   폼객체 랜더링
    if request.method == 'POST': # request의 방식이 get 방식 POST방식이 있는데 post으로 들어오면 실행
        form = CountryDataForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CountryDataForm()
    # 나라별 인구 데이터를 DB에서 가져오기
    country_datas = CountryData.objects.all()
    # print(country_datas)
    context = {
        'form': form,
        'country_datas': country_datas
    }
    return render(request, 'dashboard/dashboard.html', context)