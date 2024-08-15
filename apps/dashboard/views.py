from django.shortcuts import render
from apps.shop.models import *

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def product_list(request):
    return render(request, 'dashboard/product_list.html')

def order_list(request):

    order_items = OrderItem.objects.filter(product__company__user=request.user)

    context = {
        'order_items': order_items
    }

    return render(request, 'dashboard/order_list.html', context)
