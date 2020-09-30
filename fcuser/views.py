from django.shortcuts import render
from django.http import HttpResponse # 비밀번호 확인을 하기 위한 불러옴
from django.contrib.auth.hashers import make_password, check_password # 비밀번호 암호화 해서 저장하기 위한 make_password, 비밀번호를 비교하기 위한 check_password
from .models import Fcuser

# 이 함수가 URL에 연결 하면 요청 정보가 request 매개변수 통해서 들어 오게끔 한다.
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
        # request를 꼭 같이 전달해줘야 하고 자신이 반환하고 싶은 HTML 파일을 써주면 된다.
        # 그리고 장고는 경로를 어떻게 찾느냐 하면 저 html의 파일은 이미 장고가 templates 폴더를 바라보고 있기 때문에
        # 경로가 찾아진다.
    elif request.method == 'POST':
        username = request.POST['username']
        password =  request.POST['password']
        re_password =  request.POST['re-password']

        res_data = {}
       
        if password != re_password:
            res_data['error'] = '비밀번호가 일치하지 않습니다.'
        else:
            fcuser = Fcuser(
                username = username,
                password = make_password(password)
            )

            fcuser.save()

            return render(request, 'register.html', res_data)

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html') # 로그인 html과 연결
    elif request.method == 'POST':
        username = request.POST.get('username', None) # 입력 받은 username(id)를 username 변수에 저장, 기본값은 none
        password = request.POST.get('password', None) # 입력 받은 password를 password 변수에 저장, 기본값은 none

        res_data ={}
        if not (username and password):
            res_data['error'] = '모든 값을 입력해야합니다.'
        else:
            fcuser = Fcuser.objects.get(username = username) # 입력 받은 id와 필드명이 같은 것을 모델에서 가지고 온다.
            if check_password(password, fcuser.password):
                    # 입력 받은 비밀번호와 모델의 비밀번호가 같은 경우 로그인 처리
                    pass
            else:
                res_data['error'] = '비밀번호가 다릅니다.'
            
        return render(request, 'login.html', res_data)

            




