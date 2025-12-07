from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Order

PAYMENT_CHOICES = [
    ('bank',   'Direct Bank Transfer'),
    ('card',   'Credit / Debit Card'),
    ('cod',    'Cash on Delivery'),
    ('paypal','PayPal'),
]

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model  = User
        fields = ['username', 'email', 'password1', 'password2']

class CheckoutForm(forms.ModelForm):
    payment_method = forms.ChoiceField(choices=PAYMENT_CHOICES)

    class Meta:
        model  = Order
        fields = [
            'first_name', 'last_name',
            'street_address', 'apartment',
            'city', 'postal_code', 'country',
            'payment_method', 'order_notes',
        ]
        widgets = {
            'order_notes':    forms.Textarea(attrs={'rows':3}),
            'street_address': forms.TextInput(),
            'apartment':      forms.TextInput(),
            'city':           forms.TextInput(),
            'postal_code':    forms.TextInput(),
            'country':        forms.TextInput(),
        }
