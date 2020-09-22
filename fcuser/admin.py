from django.contrib import admin
from .models import Fcuser # models.py의 Fcuser 클래스 불러옴
# Register your models here.

class FcuserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'registered_dttm')
    # 모델에 등록된 데이터의 상세한 다른 필드도 출력하고 싶으면 자신이 list_display = ()로 써주어서 지정할 수있다.

admin.site.register(Fcuser, FcuserAdmin) 
# 이렇게 하면 관리자 페이지에 모델이 등록 됨
