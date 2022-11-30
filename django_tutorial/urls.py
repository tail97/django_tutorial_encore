"""django_tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from community.views import write,articleList,viewDetail,index



urlpatterns = [
    path('admin/', admin.site.urls), # id랑 비밀번호 설정하는 창
    path('write/',write,name='write'),# db 정보를 입력 받을 수 있는 창 
    path('list/',articleList,name="list"), # db 정보를 볼 수 있는 창
    path('view_detail/<int:num>/',viewDetail, name='view_detail'), #db정보를 세부창으로 볼 수 있는 창
    path('',index, name= "index")
]
