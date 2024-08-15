from django.urls import path
from .views import *


urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('d-product-list/', product_list, name='d-product-list'),
    path('d-order-list/', order_list, name='d-order-list'),
]