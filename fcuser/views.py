from django.shortcuts import render, redirect # 리다이랙트를 위해 불러옴
from django.http import HttpResponse # 비밀번호 확인을 하기 위한 불러옴
from django.contrib.auth.hashers import make_password, check_password # 비밀번호 암호화 해서 저장하기 위한 make_password, 비밀번호를 비교하기 위한 check_password
from .models import Fcuser
from .forms import LoginForm

# 이 함수가 URL에 연결 하면 요청 정보가 request 매개변수 통해서 들어 오게끔 한다.
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html') # 레지스터 html과 연결
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
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid(): # 유효성 검사
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def home(request):
    user_id = request.session.get('user') # 세션으로부터 사용자 정보를 가지고 옴

    if user_id: # 만약에 user가 있으면
        fcuser = Fcuser.objects.get(pk=user_id) # 모델에서 id를 가지고 옴
        return HttpResponse(fcuser.name) # 유저네임 출력
         
    return HttpResponse('Home!') # 로그인을 안했다면 홈이 나옴

            




