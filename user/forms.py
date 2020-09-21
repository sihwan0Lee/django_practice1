from django import forms
from .models import User
from django.contrib.auth.hashers import check_password


class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={'required': '아이디를 입력해주세요'}, max_length=32, label="사용자 이름")
    password = forms.CharField(error_messages={
                               'required': '아이디를 입력해주세요'}, widget=forms.PasswordInput, label="비밀번호")
# widget=forms.PasswordInput 비밀번호를 패스워드 타입으로 위젯을 직접 지정했음.
# 이제 암호도 숨겨져서 나옴
# 에러메시지 입력하는거, 방금 메시지가 리콰이어드라는 키에 들어있기떄문에 저렇게하는거임.
    # 이제 비밀번호 일치하는 여부도 확인. 이미 만들어져 있는 함수를 사용할것임 .ㄱ ㅡ래서 슈퍼를 통해 기존에 폼안에 들어있던 클린함수를 먼저호출

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                self.add_error('username', '아이디가 없습니다.')
                return
            if not check_password(password, user.password):
                # 입력받은값, 모델에 있는값
                # 폼안에 기본적으로 있는 add error 함수임. 특정 필드에 에러를 넣는 함수임
                self.add_error('password', '비밀번호가 틀렸습니다')
            else:
                # 셀프를 통해서 클래스변수안에 들어가게된다. 그럼 밖에서도 접근이 가능하다.
                self.user_id = user.id

# form 안에서 데이터를 어떻게 검증할건지에 대해서 클래스를 하나 만들게되고 뷰에서는 코드가 깔끔해짐.
# 로그인 폼을 만들고 이게 정상적인지 확인하고 정상적이라면 어디로 가라. 굉장히 심플해진다.
