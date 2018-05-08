from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, label='用户名')
    password = forms.CharField(max_length=20, label='密码', widget=forms.PasswordInput)
