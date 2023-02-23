from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render

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