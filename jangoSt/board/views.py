from django.shortcuts import render
from .models import Board
from .forms import BoardForm
# Create your views here.


def board_list(request):
    # 모든 게시물을 갖고오는데 최신걸 가져오는 함수 // "-" 는 역순 (가장최신걸 갖고오기)
    boards = Board.objects.all().order_by('-id')
    return render(request, 'board_list.html', {'boards': boards})


def board_write(request):
    form = BoardForm()
    return render(request, "board_write.html", {'form': form})
