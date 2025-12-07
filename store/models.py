from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Product(models.Model):
    BRAND_CHOICES = [
        ("Arcadio", "Arcadio"), ("Arnette", "Arnette"), ("Brooklyn", "Brooklyn"),
        ("Cameo", "Cameo"), ("Freya", "Freya"), ("Green Vision", "Green Vision"),
        ("Jacques Lamount", "Jacques Lamount"), ("Knockaround", "Knockaround"),
        ("Lazer", "Lazer"), ("LK Bennet", "LK Bennet"), ("Matrix", "Matrix"),
        ("Meridian", "Meridian"), ("Michael Kors", "Michael Kors"),
        ("O’neill", "O’neill"), ("OMG", "OMG"), ("Penguin", "Penguin"),
        ("Quicksilver", "Quicksilver"), ("Ray-Ban", "Ray-Ban"),
        ("Reserve", "Reserve"), ("Retro", "Retro"), ("Roxy", "Roxy"),
        ("Shadez", "Shadez"), ("Solano", "Solano"), ("Stepper", "Stepper"),
        ("Superdry", "Superdry"), ("Universal", "Universal"), ("Vogue", "Vogue"),
        ("Whizkids", "Whizkids"), ("Zenith", "Zenith"),
    ]

    GENDER_CHOICES = [
        ("Kids", "Kids"), ("Men", "Men"), ("Unisex", "Unisex"), ("Women", "Women")
    ]

    MATERIAL_CHOICES = [
        ("Carbon Fiber", "Carbon Fiber"), ("Mesh Band", "Mesh Band"),
        ("Metal", "Metal"), ("Metal Case", "Metal Case"), ("Plastic", "Plastic"),
        ("Steel Band", "Steel Band"), ("Steel Case", "Steel Case")
    ]

    name        = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    image       = models.ImageField(upload_to='product_images/', blank=True, null=True)
    brand       = models.CharField(max_length=50, choices=BRAND_CHOICES, default="Ray-Ban")
    gender      = models.CharField(max_length=10, choices=GENDER_CHOICES, default="Unisex")
    material    = models.CharField(max_length=50, choices=MATERIAL_CHOICES, default="Plastic")

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class CartItem(models.Model):
    cart     = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Order(models.Model):
    PAYMENT_CHOICES = [
        ('bank',   'Direct Bank Transfer'),
        ('card',   'Credit / Debit Card'),
        ('cod',    'Cash on Delivery'),
        ('paypal', 'PayPal'),
    ]

    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    payment_method  = models.CharField(max_length=30, default="Cash on Delivery")

    first_name      = models.CharField(max_length=50, null=True, blank=True)
    last_name       = models.CharField(max_length=50, null=True, blank=True)
    street_address  = models.CharField(max_length=200, null=True, blank=True)
    apartment       = models.CharField(max_length=50, null=True, blank=True)
    city            = models.CharField(max_length=100, null=True, blank=True)
    postal_code     = models.CharField(max_length=20, null=True, blank=True)
    country         = models.CharField(max_length=100, null=True, blank=True)
    order_notes     = models.TextField(blank=True, null=True)


    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

class OrderItem(models.Model):
    order              = models.ForeignKey(Order, on_delete=models.CASCADE)
    product            = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity           = models.PositiveIntegerField()
    price_at_purchase  = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} (Order #{self.order.id})"