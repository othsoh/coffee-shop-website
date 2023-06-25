from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import  render,redirect
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem, Product
from django.utils import timezone
from django.contrib import messages




# Create your views here.


def Menu(request):
    
    return render(request, 'Products/Menu.html', {'Products':Product.objects.all()})

def services(request):
    return render(request, 'Products/services.html')

@login_required(login_url="/user/login/")
def cart(request):
    cart,_ = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all() 
    total_price = calculate_total_price(cart_items)
    total_cart_item=total_items(cart_items)
    final_price=calculate_price_and_delivery(cart_items)


    context={
        'cart_items': cart_items,
        'total_price':total_price,
        'total_items':total_cart_item,
        'final_price':final_price,
    }

    return render(request, 'Products/cart.html', context)

@login_required(login_url="/user/login/")
def add_to_cart(request, product_id):

    product = Product.objects.get( id=product_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_item, _ = CartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.quantity += 1
    cart_item.save()
    
    return redirect('Menu')

@login_required(login_url="/user/login/")
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    return redirect('cart')
    

def if_quantity_i_zero(request, item_id):

    cart_item = get_object_or_404(CartItem, id=item_id)

    if cart_item.quantity <= 0:
        cart_item.delete()
        return redirect('cart')

def calculate_price_and_delivery(cart_items):
    final_price=calculate_total_price(cart_items)+10
    if final_price<=10:
        final_price=0
        
    return final_price

def calculate_total_price(cart_items):
    total_price = 0
    for cart_item in cart_items:
        total_price += cart_item.product.price * cart_item.quantity

    return total_price

def update_cart_item(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)

    if request.method=='POST':
        new_quantity=request.POST.get('quantity')
        cart_item.quantity = new_quantity

        cart_item.save()
        return redirect('cart')

def total_items(carts):
    total_cart_item=0
    for cart in carts:
        total_cart_item += 1
    return total_cart_item


def checkout(request):
    cart_items=CartItem.objects.all()
    for item in cart_items:
        remove_from_cart(request, item.id)
    

    return redirect('cart')

def reserver(request):
    return render(request,'Products/reserver.html')

