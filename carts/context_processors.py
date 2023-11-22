from .models import Cart, CartItem
from .views import _cart_id

from django.db.models import Sum
from django.shortcuts import get_object_or_404

def counter(request):
    cart_count = 0
    
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = get_object_or_404(Cart, cart_id=_cart_id(request))
            cart_count = CartItem.objects.filter(cart=cart).aggregate(total_items=Sum('quantity'))['total_items'] or 0
        except Cart.DoesNotExist:
            cart_count = 0
    
    return {'cart_count': cart_count}

