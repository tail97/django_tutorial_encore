from django.urls import path
from community.views import write,articleList,viewDetail

urlpatterns = [
    path('write/',write,name='write'),# db 정보를 입력 받을 수 있는 창 
    path('list/',articleList,name="list"), # db 정보를 볼 수 있는 창
    path('view_detail/<int:num>/',viewDetail, name='view_detail'), #db정보를 세부창으로 볼 수 있는 창
]