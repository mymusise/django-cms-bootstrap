from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(User)
class User(admin.ModelAdmin):
    pass

@admin.register(LoginHistory)
class LoginHistory(admin.ModelAdmin):
    pass