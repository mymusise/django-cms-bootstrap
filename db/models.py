from django.db import models
from django.utils import timezone
# Create your models here.
class User(models.Model):
    username            = models.CharField(max_length=32)
    email               = models.CharField(max_length=16)
    sex                 = models.IntegerField(default=0)
    password_salt       = models.CharField(max_length=16)
    password_encryption = models.CharField(max_length=64)
    is_email_verified   = models.BooleanField(default=False)
    is_phone_verified   = models.BooleanField(default=False)
    is_user_enable      = models.BooleanField(default=True)
    email_verification_code = models.CharField(max_length=32)
    phone_verification_code = models.CharField(max_length=32)
    reset_password_code = models.CharField(max_length=32)
    create_at           = models.DateTimeField(default=timezone.now)

class LoginHistory(models.Model):
    uid                 = models.ForeignKey(User)
    token               = models.CharField(max_length=64)
    ip                  = models.CharField(max_length=64)
    device              = models.CharField(max_length=64)
    time_out            = models.DateTimeField(max_length=64)
    create_at           = models.DateTimeField(default=timezone.now)
