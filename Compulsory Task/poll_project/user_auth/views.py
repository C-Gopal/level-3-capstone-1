from django.shortcuts import render
from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def user_login(request):
    return render(request, 'authentication/login.html')

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username = username, password = password)

    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:login')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('polls:polls')
        )

def show_user(request):
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        'username': request.user.username,
        'password': request.user.password,
    })

# the signup page is not functional but once the fields are filled out, the signup button works
def signup(request):
    return render(request, "registration/signup.html")