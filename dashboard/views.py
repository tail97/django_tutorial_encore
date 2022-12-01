from django.shortcuts import render, redirect
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
    if request.method == 'POST':  # request의 방식이 get 방식 POST방식이 있는데 post으로 들어오면 실행
        form = CountryDataForm(request.POST)
        if form.is_valid():  # 데이터가 들어오는걸 확인.
            print(form)
            '''
            폼에 입력 값을 개별로 변수 대입
            나라이름 (country) DB 값이 있는 지 확인
            입력한 나리 이름이 있으면 , 업데이트하고 
            없으면 저장
            '''
            input_country = form.data.get(
                "country", None)  # country가 있으면 value를 가져오고 없으면 none
            input_num = form.data.get("population", None)
            CountryData.objects.update_or_create(
                # filter
                country=input_country,  # 비교하는 코드
                # new value
                defaults={  # 없으면 업데이트
                    'country': input_country,
                    'population': input_num
                }
            )
            # form.save()
            # return redirect("/dashboard") # 입력창에 있는 데이터 없어진다.
            return redirect(".")  # 입력창에 있는 데이터 없어진다. 둘다 똑같은것 .
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
