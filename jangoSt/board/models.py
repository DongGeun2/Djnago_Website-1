from django.db import models

# Create your models here.


class Board(models.Model):
    title = models.CharField(max_length=128, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    writer = models.ForeignKey('fcuser.Fcuser', on_delete=models.CASCADE,
                               verbose_name='작성자')
    reqistered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return self.title

    class Meta:    # 데이터 베이스에 테이블 명을 지정할때 사용
        db_table = 'fastcampus_board'
        verbose_name = '게시글'
        verbose_name_plural = '게시글'
