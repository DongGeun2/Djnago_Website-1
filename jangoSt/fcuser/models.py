from django.db import models


class Fcuser(models.Model):
    username = models.CharField(max_length=32, verbose_name='사용자명')
    useremaill = models.EmailField(max_length=128, verbose_name='사용자이메일')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    reqistered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return self.username

    class Meta:    # 데이터 베이스에 테이블 명을 지정할때 사용
        db_table = 'fastcampus_fcuser'
        verbose_name = '패스트 캠퍼스 사용자'
        verbose_name_plural = '패스트 캠퍼스 사용자'


# py manage.py makemigrations  - 마이그레이션 파일 (초안) 생성하기.
# py manage.py migrate     - 마이그레이션 파일 DB에 반영하기.
# 만든 모델을 init이라는 파일로 DB를 만들어줌
