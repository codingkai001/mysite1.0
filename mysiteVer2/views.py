from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render_to_response, render
from django.contrib import auth
from django.urls import reverse
from .forms import LoginForm


def index(request):
    context = dict()
    return render_to_response('index.html', context)


def login(request):
    # username = request.POST.get('username')
    # password = request.POST.get('password')
    # user = auth.authenticate(request, username=username, password=password)
    # referer = request.META.get('HTTP_REFERER', reverse('home'))
    # if user is not None:
    #     auth.login(request, user)
    #     return HttpResponseRedirect(referer)
    # else:
    #     return render(request, 'error.html', {'message': '用户名或密码不正确'})

    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect(request.GET.get('from', reverse('home')))
            else:
                login_form.add_error(None, '用户名或密码不正确')
        else:
            login_form = LoginForm()

    else:
        login_form = LoginForm()

    context = dict()
    context['login_form'] = login_form
    return render(request, 'login.html', context)


