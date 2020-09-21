from django.shortcuts import render, redirect
from .models import User
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .forms import LoginForm
# 장고에 이미 포함되있는 ...이안에 check password도 있음 hasher 안에
# Create your views here.


def home(request):
    user_id = request.session.get('user')
    if user_id:
        user = User.objects.get(pk=user_id)
        # return HttpResponse(user.username)
    # return HttpResponse('HOME')
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():                 # form 에 기본적으로 있는 함수임 . form에 데이터를 넣으면 여기서 검사가 될것임.
            # 메시지도 필요해서 login.html에 추가해줫음 레드부분. 함수의 기능임.

            # 세션  (세션에 데이터넣을땐 키를넣고..아이디가 없으니 가져와야함.)
            request.session['user'] = form.user_id  # is valid에 의해 이미 검증이된거임
            return redirect('/')
    else:
        form = LoginForm()
    # if request.method == 'GET':
    #    return render(request, 'login.html')  # 연결
    # elif request.method == 'POST':
    #    username = request.POST.get('username', None)
    #    password = request.POST.get('password', None)

    #    res_data = {}
    #   if not (username and password):
    #      res_data['error'] = "값이 누락되었습니다."
    # else:
    #    # (필드명 = 값) 입력받은 유저네임을 유저네임이라는 변수에 담아놨기때문에 .현재.
    #    user = User.objects.get(username=username)
    #    # (입력받은 비밀번호, 모델로부터 가져온 비밀번호값.)
    #    if check_password(password, user.password):
    #        request.session['user'] = user.id
    #        # 방금 로그인한 유저의 아이디값을 세션에 저장한것임. 넣은거로만 저장이됌
    #        return redirect('/')  # 일반적으로 / 로해두면 만들고있는 웹의 홈으로 간다.
    #        # 비밀번호가 일치하면 로그인처리
    #        # 진짜 로그인처럼되려면 세션이 필요함.
    #        # 로그인이 끝났으면 이제 다른 창으로 가야지 홈으로 가던가. redirect

    # pass
    #    else:
    #        res_data['error'] = " 비밀번호 틀림"
    # return render(request, 'login.html', res_data)
    return render(request, 'login.html', {'form': form})
    # 메세지를 전달하기 위해 렌더를 할때  딕셔너리변수를 전달하기 위해 res_data를 추가.


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
        # 아직 아무것도 전달한 데이터가 없어서 처음 접속했을때 나오는것임.
    elif request.method == "POST":
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)
        # 딕셔너리에서 그 키값을 가지고 오는데 그 키값없으면 기본값으로 none으로 지정.
        # 근데 [] 였다가 () 로 바꿔버리는이유점
        # 그리고 get을 갑자기 왜 붙임.
        # 만약에 사용자이름 비번, 비번확인 다 입력안하고 포스트요청하면 에러안날것임.
        # 그냥 빈문자열들로 사용자가 생성될것이기 떄문에
        # 입력받은값에 대한 예외처리를 한것임.
        # 딕셔너리라 키가없으면 에러가 나니까, 겟함수를 사용해서 기본값을 지정한다.

        res_data = {}

        if not (username and password and re_password and useremail):
            res_data['error'] = '값이 누락되었습니다.'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:

            user = User(
                username=username,
                useremail=useremail,
                password=make_password(password)  # 암호화하고나서 저장
            )

            user.save()

        return render(request, 'register.html', res_data)
        # register.html 을 렌더링 할때 그러니까 페이지 전달할떄 데이터 넘길때 res_data가 매핑이 된다이거임
        #
