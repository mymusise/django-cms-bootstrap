from django.shortcuts import render

# Create your views here.

def SignIn(req):
    return render(req,'account/sign-in.html')

def SignUp(req):
    return render(req,'account/sign-up.html')