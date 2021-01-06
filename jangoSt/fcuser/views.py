from django.shortcuts import render, redirect
from .models import Fcuser
from django.contrib.auth.hashers import make_password, check_password  # 비밀번호 암호화
from django.http import HttpResponse
from .forms import LoginForm
# Create your views here.


def home(request):
    user_id = request.session.get('user')

    if user_id:
        fcuser = Fcuser.objects.get(pk=user_id)
        return HttpResponse(fcuser.username)

    return HttpResponse('home')


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect("/")


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id

            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


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
            return HttpResponse("회원가입이 완료되었습니다.")
        return render(request, 'register.html', res_date)
