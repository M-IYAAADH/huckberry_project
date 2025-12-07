from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CheckoutForm
from .models import Product, Cart, CartItem, Order, OrderItem

def home(request):
    return render(request, 'store/home.html')

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'store/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'store/login.html', {'error': 'Invalid credentials'})
    return render(request, 'store/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def product_list(request):
    selected_brands    = request.GET.getlist('brand')
    selected_genders   = request.GET.getlist('gender')
    selected_materials = request.GET.getlist('material')

    products = Product.objects.all()
    if selected_brands:
        products = products.filter(brand__in=selected_brands)
    if selected_genders:
        products = products.filter(gender__in=selected_genders)
    if selected_materials:
        products = products.filter(material__in=selected_materials)

    return render(request, 'store/products.html', {
        'products': products,
        'selected_brands': selected_brands,
        'selected_genders': selected_genders,
        'selected_materials': selected_materials,
        'Product': Product, 
    })


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('product_list')

login_required
def view_cart(request):
    cart, _     = Cart.objects.get_or_create(user=request.user)
    raw_items   = CartItem.objects.filter(cart=cart)
    total       = 0
    cart_items  = []
    for item in raw_items:
        item.subtotal = item.product.price * item.quantity
        total += item.subtotal
        cart_items.append(item)
    return render(request, 'store/view_cart.html', {
        'cart_items': cart_items,
        'total': total
    })

@login_required
def update_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    if request.method == 'POST':
        if 'increment' in request.POST:
            cart_item.quantity += 1
        elif 'decrement' in request.POST and cart_item.quantity > 1:
            cart_item.quantity -= 1
        elif 'quantity' in request.POST:
            try:
                new_qty = int(request.POST.get('quantity', cart_item.quantity))
                if new_qty > 0:
                    cart_item.quantity = new_qty
            except ValueError:
                pass
        cart_item.save()
    return redirect('view_cart')

@login_required
def remove_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    return redirect('view_cart')

@login_required
def checkout(request):
    cart, _     = Cart.objects.get_or_create(user=request.user)
    cart_items  = CartItem.objects.filter(cart=cart)
    total       = sum(item.product.price * item.quantity for item in cart_items)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid() and cart_items.exists():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price_at_purchase=item.product.price
                )
            cart_items.delete()
            return render(request, 'store/checkout_success.html', {'order': order})
    else:
        form = CheckoutForm()

    return render(request, 'store/checkout.html', {
        'form':       form,
        'cart_items': cart_items,
        'total':      total,
    })

def about(request):
    return render(request, 'store/about.html')

def privacy_policy(request):
    return render(request, 'store/privacy.html')

def contact(request):
    if request.method == 'POST':
        return render(request, 'store/contact_success.html')
    return render(request, 'store/contact.html')