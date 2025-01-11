from django.urls import path 
from . import views  

urlpatterns = [
    path('', views.index, name='index'),
    path('orders/', views.OrderListCreate.as_view(), name='order-list'),
    path('orders/<int:pk>/', views.OrderUpdate.as_view(), name='update-order'),
    path('orders/delete/<int:pk>/', views.OrderDelete.as_view(), name='order-delete'),
]