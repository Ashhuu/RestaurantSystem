from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.orderDetails, name="order"),
    path('ordercomplete/<oid>/', views.orderId, name="orderid"),
]
