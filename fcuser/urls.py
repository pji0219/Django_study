from django.urls import path
from . import views
# 현재 경로의 뷰 파일을 불러옴

urlpatterns = [
    path('register/', views.register),
    path('login/' , views.login),
    # 경로로는 레지스터를 사용하고 뷰 파일의 레지스터 함수 연결
]
