from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^sign-in/', views.SignIn),
    url(r'^sign-up/', views.SignUp),
]
