from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage

def login(request):
    if request.method == 'POST':
        username = request.POST['userName']
        password = request.POST['passWord']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if (request.user.is_authenticated):
                return redirect('nhasi')
        else:
            messages.error(request, 'Đăng nhập thất bại')
            return redirect('login')
    else:
        return render(request, 'loginview/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        # messages.success(request, 'You are now logged out')
        return redirect('login')

