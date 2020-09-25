from django.shortcuts import render

# Create your views here.

# 이 함수가 URL에 연결 하면 요청 정보가 request 매개변수 통해서 들어 오게끔 한다.
def register(request):
    return render(request, 'register.html')
    # request를 꼭 같이 전달해줘야 하고 자신이 반환하고 싶은 HTML 파일을 써주면 된다.
    # 그리고 장고는 경로를 어떻게 찾느냐 하면 저 html의 파일은 이미 장고가 templates 폴더를 바라보고 있기 때문에
    # 경로가 찾아진다.
