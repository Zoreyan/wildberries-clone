from .models import Order

def get_cart_total(request):
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        return order.get_cart_total
    else:
        return 0