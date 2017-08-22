# coding=utf8
from  django import forms
from .models import UserModel

class LoginForm(forms.ModelForm):

    class Meta:
        model = UserModel
        fields = ['name', 'password']
        labels = {'name': '用户名','password': '密码'}
        widgets = {'name':forms.TextInput(attrs={'cols':50}),'password':forms.PasswordInput(attrs={"cols":16})}