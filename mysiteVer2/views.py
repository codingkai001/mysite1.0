from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.models import User


def sign_in(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        username = request.POST.get('username')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('blog:article_list'), request)
        else:
            return render(request, 'sign_in.html', {'status': '用户名或密码不正确！'})
    else:
        return render(request, 'sign_in.html')


def sign_out(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home'))


def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)
            return render(request, 'sign_up.html', {'status': '用户名已存在！'})
        except User.DoesNotExist:
            password = request.POST.get('password')
            email = request.POST.get('email')
            user = User()
            user.username = username
            user.set_password(password)
            user.email = email
            user.save()
            return HttpResponseRedirect(reverse('blog:article_list'))
    else:
        return render(request, 'sign_up.html')


def profile(request, username):
    # 请求查看用户数据
    if request.method == 'GET':
        try:
            user = User.objects.get(username=username)
            return render(request, 'profile.html', {'user': user})
        except User.DoesNotExist:
            return HttpResponseRedirect('/blog')

    # 修改用户数据
    else:
        pass
