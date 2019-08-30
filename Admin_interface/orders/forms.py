from django import forms
from orders.models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=('name','phone','email','address','city','pincode','state')