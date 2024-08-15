from django.urls import path
from .views import *


urlpatterns = [
    path('', product_list, name='product-list'),
    path('catalog/<int:pk>/', product_detail, name='product-detail'),
    path('company/<int:pk>/', company_products, name='company-products'),
    path('catalog/<slug:slug>/', category_catalog, name='category-catalog'),
    path('cart-page/', cart_page, name='cart-page'),
    path('shipping-address/', shipping_address_page, name='shipping-address'),
    path('pending-page/', pending_page, name='pending-page'),
    path('process-order/', process_order, name='process-order'),
    path('become-seller-page/', become_seller_page, name='become-seller-page'),
]