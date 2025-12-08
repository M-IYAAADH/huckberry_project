"""
Context processors for the store app.
"""
from django.db.models import Sum
from .models import Cart, CartItem


def cart_context(request):
    """
    Add cart item count to all template contexts.
    """
    cart_item_count = 0

    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            agg = CartItem.objects.filter(cart=cart).aggregate(
                total_qty=Sum('quantity')
            )
            cart_item_count = agg['total_qty'] or 0

    return {
        'cart_item_count': cart_item_count,
    }
