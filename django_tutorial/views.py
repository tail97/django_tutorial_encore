from django.views.generic.base import TemplateView
from django.views.generic import CreateView, ListView, DetailView # 새로운 레코드 생성을 위한 폼 뷰 보임, 테이블 레코드 생성
from django.urls import reverse_lazy
from .forms import CreateUserForm
from community.models import Article


class UserCreateView(CreateView):
    form_class = CreateUserForm #forms.py에 정의 되어 있는 form클래스
    template_name = 'registration/register.html'
    # 폼에 입력 된 내용에 에러가 없고, 테이블 레코드 생성이 완료된 후에 이동할 URL을 지정함.
    # success_url = 'done/'
    success_url = reverse_lazy('register_done') # 데이터가 들어오면 DB에 저장하기위한코드
    # url패턴 전달인자, urls.py 모듈이 메모리 로딩된 후에 실행

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'