from django import forms
from orderentry.models import customerInfo, orderInfo
from inventory.models import flavor, sizes, shipping

class customerOrder(forms.ModelForm):
    
    order_Item_Flavor = flavor
    order_Sizes = sizes
    order_Quantity = orderInfo.order_Quantity
    order_Shipping = shipping

    class Meta:
        model = orderInfo
        fields = ['order_Item_Flavor','order_Sizes', 'order_Quantity', 'order_Shipping']

        def __init__(self, *args, **kwargs) -> None:
            super(sizes, self).__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs = {'class': 'form-control'}

class customerInfo(forms.ModelForm):
    
    customer_first_name = forms.CharField(max_length=30, label='First Name')
    customer_last_name = forms.CharField(max_length=30, label='Last Name')
    shipping_address = forms.CharField(max_length=60, label='Shipping Address')
    billing_address = forms.CharField(max_length=60, label='Billing Address')

    class Meta:
        model = customerInfo
        fields = ['customer_first_name','customer_last_name','shipping_address', 'billing_address']
        