from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *


def appofimage(request):
    cats = category.objects.all()
    images = post.objects.all()
    data = {'images': images, 'cats': cats}
    return render(request, 'home.html', data)


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, 'user has been created')
        return redirect('appofimage')
    else:
        return render(request, 'signup.html')


def login(request):
    return render(request, 'login.html')
