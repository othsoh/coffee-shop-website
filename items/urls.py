from django.urls import path
from . import views



urlpatterns = [
    path('menu/', views.Menu, name="Menu"),
    path('services/', views.services, name="services"),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update_cart_item/<int:cart_item_id>/', views.update_cart_item,name="update_cart"),
    path('checkout/',views.checkout,name="checkout"),
]