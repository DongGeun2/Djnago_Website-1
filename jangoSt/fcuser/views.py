from django.shortcuts import render
from .models import Fcuser
from django.contrib.auth.hashers import make_password  # 비밀번호 암호화
from django.http import HttpResponse

# Create your views here.


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_date = {}

        if not (username and useremail and password and re_password):
            res_date['error'] = '모든 값을 입력해야합니다.'

        elif password != re_password:
            res_date['error'] = '비밀번호가 다릅니다.'

        else:
            fcuser = Fcuser(
                username=username,
                useremaill=useremail,
                password=make_password(password)
            )

            fcuser.save()

        return render(request, 'register.html', res_date)
