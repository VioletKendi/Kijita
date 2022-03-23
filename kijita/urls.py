from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name= "index"),
    path("Signup", views.signup, name ="signup" ),
    path("LogIn", views.login, name="login"),
]