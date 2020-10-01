from django.db import models

class Fcuser (models.Model): # 클래스를 만들고 models.Model을 상속 받아야한다.
    objects = models.Manager()
    username = models.CharField(max_length=64, verbose_name='사용자명')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return self.username
    # 원래 관리자 페이지에서 나오는 사용자 목록의 이름은 모델 파일 안의 클래스를 문자열로 나타냈을 때 나오는 값인데
    # 파이썬에는 이 클래스가 문자열로 변환 되었을 때 어떻게 변환할 지를 정하는 내장함수를 가지고 있는데 그것이 이 함수이다.
    # 그래서 self.username으로 내가 설정한 username으로 변환하겠다고 설정한 것

    class Meta:
        db_table = 'fc_person'
    # 자신이 별도의 테이블명을 만들고 싶으면 클래스 안의 클래스로 선언해줘야함 
        verbose_name = '홈페이지 사용자'
        # 관리자 페이지에서 나오는 모델명을 바꿀 수 있음
        verbose_name_plural = '홈페이지 사용자'
        # 복수형을 단수형으로 바꿈

    
