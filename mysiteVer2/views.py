from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render_to_response, render
from django.contrib import auth
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.models import User


def sign_in(request):
    return render(request, 'sign_in.html')
    # if request.method == 'POST':
    #     login_form = LoginForm(request.POST)
    #     if login_form.is_valid():
    #         username = login_form.cleaned_data['username']
    #         password = login_form.cleaned_data['password']
    #         user = auth.authenticate(request, username=username, password=password)
    #         if user is not None:
    #             auth.login(request, user)
    #             return redirect(request.GET.get('from', reverse('home')))
    #         else:
    #             login_form.add_error(None, '用户名或密码不正确')
    #     else:
    #         login_form = LoginForm()
    #
    # else:
    #     login_form = LoginForm()
    #
    # context = dict()
    # context['login_form'] = login_form
    # return render(request, 'sign_in.html', context)


def sign_out(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home'))


def sign_up(request):
    return render(request, 'sign_up.html')
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     user_exists = User.objects.filter(username=username)
    #     if user_exists:
    #         return render(request, 'sign_up.html', {'error': '用户名已存在！'})
    #     else:
    #         new_user = User()
    #         new_user.username = username
    #         new_user.password = request.POST.get('password')
    #         new_user.email = request.POST.get('email')
    #         new_user.save()
    # else:
    #     return render(request, 'sign_up.html')
