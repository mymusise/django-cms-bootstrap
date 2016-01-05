from django.shortcuts import render

# Create your views here.

def SignIn(req):
    return render(req,'account/sign-in.html')

def SignUp(req):
    return render(req,'account/sign-up.html')

def ResetPassword(req):
    return render(req,'account/reset-password.html')

def ForgetPassword(req):
    return render(req,'account/forget-password.html')
