from django.shortcuts import render
from .models import Board

def board_list(request):
    boards = Board.objects.all().order_by('-id') # Board 모델의 모든 게시물을 가지고 오고, -id에서 -가 의미하는거는 역순 즉 가장 최신 것을 먼저 가지고 오겠다.
    return render(request, 'board_list.html', {'boards': boards}) # {'boards': board} 템플릿에 전달