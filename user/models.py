from django.db import models

# Create your models here.


class User(models.Model):  # 클래스 만들때 장고에서 제공하는 모델스의 모델을 상속받아야함.
    username = models.CharField(max_length=34, verbose_name='사옹자명')
    useremail = models.EmailField(max_length=128, verbose_name='사용자 이메일')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='등록시간')
    # dttm = date time
    # verbose_name 의 설정으로 admin 사이트에 나오는 이름명 설정이됌.
    # 이메일필드라고 보통사용한다고함.

    def __str__(self):
        return self.username
    # user object 라고 나오던게 이제 username 의 객체 으로 나옴
    # 파이썬에는 클래스가 문자열로 변환됬을떄 어떻게 변환을 할지 결정하는 내장함수가 있고,
    # 그것이 __str__ 이다.
    # 내가 가진 유저네임으로 반환하겠다고 설정하는거임.
    # 그러면 이제 RM이라고 잘나옴.

    class Meta:
        db_table = 'sihwan_user'
        verbose_name = 'BTS'
        verbose_name_plural = 'BTS'  # 복수형제거
# 테이블명을 지정하는 이유
# 기본적으로 생성되는 앱들과 구분해서 테이블명을 만들기 위함임.
