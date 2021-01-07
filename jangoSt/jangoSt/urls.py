from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fcuser.urls')),

]


# py manage.py createsuperuser       어드민 아이디 만드는 명령어
