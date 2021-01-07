from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register),  # 경로 다음 ,뒤에는 함수를 정의해준다.
    path('login', views.login),
    path('logout', views.logout),
    path('home_login', views.home),
    path('home', views.home)
]
