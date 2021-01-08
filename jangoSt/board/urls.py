from django.urls import path, include
from . import views

urlpatterns = [
    path('list/', views.board_list),
    path('write/', views.board_write)
]


# py manage.py createsuperuser       어드민 아이디 만드는 명령어
