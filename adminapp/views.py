# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from adminapp.models import UserModel
from .forms import LoginForm
from adminapp.contrib.backends import UserBackend
# Create your views here.
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout


def index(request):
    if request.method=="GET":
        form=LoginForm()
        return render(request, 'adminapp/login.html', context={'register':form})
    else:
        user = authenticate(request)
        print request.session.session_key,'session'

        print dir(request.session)
        if user:
            login(request,user)
            print user.id,user.name
            print request.path
        name = request.POST.get('name', None)
        password = request.POST.get('password', None)
        return redirect('/app/admin',args=[])
@login_required(redirect_field_name='next')
def admin(request):
    print request.session.session_key
    print dir(request.session)

    return render(request,'adminapp/nav.html')

@login_required
def account(request):
    request.session.set_expiry(5)
    print dir(request.session.get_expiry_date)
    print dir(request.session.get_expiry_age)
    return HttpResponse("这个页面只有登陆用户才能访问")