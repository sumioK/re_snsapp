from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db import IntegrityError
from django.shortcuts import render, redirect

def signupfunc(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    try:
      user = User.objects.create_user(username, '', password)
      return render(request, 'signup.html',{})

    except IntegrityError:
      return render(request, 'signup.html',{'error': 'このユーザー名は既に使用されています'})
  return render(request, 'signup.html',{})

def loginfunc(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return render(request, 'login.html', {'context': 'logged in'})
    else:
      return render(request, 'login.html', {'context':'not loged in'})
    pass

  return render(request,'login.html', {'context':'get method'})