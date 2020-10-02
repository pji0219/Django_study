from django.db import models

class Board (models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=128, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    writer = models.ForeignKey('fcuser.Fcuser', on_delete= models.CASCADE, verbose_name='작성자')
    # foreignkey DB에 있는 아이디를 연결, fcuser앱에 있는 Fcuser 모델과 연결 하겠다. CASCADE: 사용자가 탈퇴하면 사용자 정보가 삭제되는데 게시글도 함께 삭제 하겠다.
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'fc_board'
        verbose_name = '홈페이지 게시글'
        verbose_name_plural = '홈페이지 게시글'

