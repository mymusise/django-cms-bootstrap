from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings

def check_parameters(method,html,*args):
    '''A warpper to chick post form parameters,
        which will return a error message when parameters not enough.
    '''
    def _check_parameters(func):
        def warpper(request,**kwargs):
            if method == "GET" and request.method == "GET":
                for key in args:
                    value = request.GET.get(key)
                    if not value:
                        message = "parameters not enough,[%s]"%key
                        return render(request,html, {'message': message})
            elif method == "POST" and request.method == "POST":
                for key in args:
                    value = request.POST.get(key)
                    if not value:
                        message = "parameters not enough,[%s]"%key
                        return render(request,html, {'message': message})
            return func(request,**kwargs)
        return warpper
    return _check_parameters

def SentSignUpMail(verification,user):
    send_mail("Sign-up","click this link to login:http://%s/account/sign-up/activate/%s"%(settings.HOST,verification.email_verification_code),"server_ping@163.com",["604072107@qq.com"])

def GetFormDate(req,dicts):
    if req.method == "POST":
        form = {}
        for dic in dicts:
            form[dic] = req.POST.get(dic)
        return form

def SignInFormCheck(form):
    message = ''
    if not form['username']:
        message = 'Please Enter Your Username!'
    elif not form['password']:
        message = 'Please Enter Your Password!'
    return message

def SignUpFormCheck(form):
    message = ''
    if not form['username']:
        message = 'Please Enter A Username!'
    elif not form['email']:
        message = 'Please enter your Email!'
    elif not form['password']:
        message = 'Please enter your Password!'
    elif form['password'] != form['passwordAgain']:
        message = 'Please enter the same Password!'
    return message