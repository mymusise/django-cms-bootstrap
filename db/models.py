from django.db import models

# Create your models here.
class User(models.Model):
    username            = models.CharField(max_length=32)
    email               = models.CharField(max_length=16)
    sex                 = models.IntegerField(default=0)
    create_at           = models.DateTimeField(default=timezone.now)

class EmailVerification(models.Model):
    Email_number            = models.CharField(max_length=16)
    Email_verification_code = models.CharField(max_length=6)
    create_at               = models.DateTimeField(default=timezone.now)

class LoginHistory(models.Model):
    uid                 = models.ForeignKey(User)
    token               = models.CharField(max_length=64)
    ip                  = models.CharField(max_length=64)
    device              = models.CharField(max_length=64)
    time_out            = models.DateTimeField(max_length=64)
    create_at           = models.DateTimeField(default=timezone.now)
