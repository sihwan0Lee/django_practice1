from django.contrib import admin
from .models import User
# Register your models here.

# admin사이트 커스터마이징


class SiUser(admin.ModelAdmin):
    list_display = ('username', 'password')   # 튜플
    # 이걸로 이제 admin 페이지의 필드명\\그거도이제 내가 설정한거로 바뀜.


admin.site.register(User, SiUser)

# User 은 임포트해온 모델명 , SiUser 은 admin의 걍 패스시킬 클래스임 . 두개가 같으니 오류가남
