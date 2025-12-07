# store/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('',                            views.home,               name='home'),
    path('signup/',                     views.signup_view,        name='signup'),
    path('login/',                      views.login_view,         name='login'),
    path('logout/',                     views.logout_view,        name='logout'),

    # Product detail page (one per sunglass)
    path('products/<int:product_id>/',  views.product_detail,     name='product_detail'),

    # Product list (grid of all sunglasses)
    path('products/',                   views.product_list,       name='product_list'),

    # Cart operations
    path('cart/add/<int:product_id>/',  views.add_to_cart,        name='add_to_cart'),
    path('cart/',                       views.view_cart,          name='view_cart'),
    path('cart/update/<int:item_id>/',  views.update_cart_item,   name='update_cart_item'),
    path('cart/remove/<int:item_id>/',  views.remove_cart_item,   name='remove_cart_item'),

    # Checkout and static pages
    path('checkout/',                   views.checkout,           name='checkout'),
    path('about/',                      views.about,              name='about'),
    path('privacy/',                    views.privacy_policy,     name='privacy'),
    path('contact/',            views.contact,         name='contact'),
]
