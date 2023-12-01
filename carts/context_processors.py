from .models import Cart, CartItem
from .views import _cart_id

from django.db.models import Sum
from django.shortcuts import get_object_or_404

from .models import Cart, CartItem

def counter(request):
    cart_count = 0

    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)
            cart_count = sum(item.quantity for item in cart_items)
        except Cart.DoesNotExist:
            cart_count = 0
    return {'cart_count': cart_count}


