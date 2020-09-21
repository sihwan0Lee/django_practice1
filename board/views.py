from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404
from user.models import User
from .models import Board
from tag.models import Tag
from .forms import BoardForm

# Create your views here.


def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다.')

    return render(request, 'board_detail.html', {'board': board})


def board_write(request):
    # 로그인 안된사람은 write 로 못감.
    if not request.session.get('user'):
        return redirect('/user/login')

    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            user = User.objects.get(pk=user_id)
            # 이미 있는 태그면 가져오고, 새로운건 생성.
            tags = form.cleaned_data['tags'].split(',')

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = user
            board.save()
            # 실제로 보드가 생성되서 저장이되면 내부적으로 아이디가 생성이되고 (pk) 아이디값이 생성된뒤에 태그를 추가해야함.
            for tag in tags:
                if not tag:
                    continue
                # 장고함수 get_or_create 사용
                # 내부안에서 쓰일용도로 _변수명 으로 만들겟음.
                # _tag, created = Tag.objects.get_or_create(name=tag)
            # name=tag 조건에 일치하는게 있으면 가져오고, 없으면 생성해서 가져옴.
            # (name=tag, writer=writer), (name=tag, default=('wr))
            # 두개를 반환을 하는데, 하나는생성된개체(_tag), 하나는 새로 생성된앤지 아닌지 여부를 가져다줌.(created)
            # 근데 지금 필요한기능은아니니까, 사용하지 않는 변수 취급 ( _) 을 해두자.
                _tag, _ = Tag.objects.get_or_create(name=tag)
                board.tags.add(_tag)

            return redirect('/board/list/')
    else:
        form = BoardForm()
    return render(request, 'board_write.html', {'form': form})


def board_list(request):
    all_boards = Board.objects.all().order_by('-id')  # 정렬 오더바이  - 는 역순
    # get 형태로 p 형태로 받겠음. 페이지번호가 p라는 값으로 받을거고 없다면 1로 하겠다.
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_boards, 5)    # 페이지당 글갯수
    boards = paginator.get_page(page)
    return render(request, 'board_list.html', {'boards': boards})
    # 기존에는 보즈라는 변수가 보드 오브젝트얼해서 나온 커리쉣의 형태였는데 이제 페이지네이터으로 가져왔기때문에
    # 이 변수 안에 이미 페이지에 대한 정보가 들어 있게 된다.
# 태그도 또다른 모델이라 그냥 추가하는게 아니라 모델을 만들어주고 추가해줘야함.
