from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.register, name="register"),
    path('login/', views.signin, name="login"),
    path('logout/', views.signout, name="logout")
]
