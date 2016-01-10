from django.contrib.auth.hashers import (make_password,check_password)
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from db.models import *
from datetime import datetime
# Create your views here.

def SignIn(req):
    if req.method == "GET":
        return render(req,'account/sign-in.html')
    elif req.method == "POST":
        message = ""
        form = {
                'username'      : req.POST.get('username'),
                'password'      : req.POST.get('password'),
            }
        if not form['username']:
            message = 'Please Enter Your Username!'
        elif not form['password']:
            message = 'Please Enter Your Password!'
        if message :
            return render(req,'account/sign-in.html',{"form":form,'message':message})

        if req.POST.get('username') and req.POST.get('password'):
            users = User.objects.filter(username=form['username'])
            if users:
                user = users.first()
                if check_password(form['password'],user.password_encryption):
                    history = LoginHistory()
                    history.uid = user
                    history.token = get_random_string(64)
                    history.time_out = datetime.now()
                    history.save()
                    res = HttpResponseRedirect('/home')
                    res.set_cookie('token',history.token,3600)
                    return res
                else:
                    message = "Password Error!"
            else:
                message = "User not exit!"
        return render(req,'account/sign-in.html',{"form":form,'message':message})

def SignUp(req):
    if req.method == "GET":
        return render(req,'account/sign-up.html')
    elif req.method == "POST":
        message = ""
        form = {
                'username'      : req.POST.get('username'),
                'email'         : req.POST.get('email'),
                'password'      : req.POST.get('password'),
                'passwordAgain' : req.POST.get('passwordAgain'),
            }
        if not form['username']:
            message = 'Please Enter A Username!'
        elif not form['email']:
            message = 'Please enter your Email!'
        elif not form['password']:
            message = 'Please enter your Password!'
        elif form['password'] != form['passwordAgain']:
            message = 'Please enter the same Password!'
        if message:
            return render(req,'account/sign-up.html',{"form":form,'message':message})
        if req.POST.get('username') and req.POST.get('email') and req.POST.get('password') and req.POST.get('passwordAgain'):
            newUser = User()
            newUser.username            = form['username']
            newUser.email               = form['email']
            newUser.password_salt       = get_random_string(16)
            newUser.password_encryption = make_password(form['password'],salt=newUser.password_salt)
            newUser.save()
            emailVerify         = EmailVerification()
            emailVerify.uid     = newUser
            emailVerify.email_verification_code = get_random_string(32)
            emailVerify.save()
            return HttpResponseRedirect('/account/sign-in')
        else:
            return render(req,'account/sign-up.html',{"form":form})

def EmailVerify(req,emailVerifyCode):
    verifications = EmailVerification.objects.filter(email_verification_code=emailVerifyCode)
    if verifications:
        verification = verifications.first()
        user = verification.uid
        user.is_email_verified = True
        user.save()
        verification.delete()
        return HttpResponse('Verify Success!')
    else:
        return HttpResponse('Verify Error!')


def ResetPassword(req):
    if req.method == "GET":
        return render(req,'account/reset-password.html')

def ForgetPassword(req):
    if req.method == "GET":
        return render(req,'account/forget-password.html')
