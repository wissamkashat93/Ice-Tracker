from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
import orderentry
from orderentry.models import orderInfo
from orderentry.forms import customerInfo, customerOrder

def getCustomerOrder(request):
    form = customerOrder(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            orderentry.forms.order_Item_Flavor = form.cleaned_data['order_Item_Flavor']
            orderentry.forms.order_Sizes = form.cleaned_data['order_Sizes']
            orderentry.forms.order_Quantity = form.cleaned_data['order_Quantity']
            orderentry.forms.order_Shipping = form.cleaned_data['order_Shipping']
            order = orderInfo.objects.filter(order_Item_Flavor = form.cleaned_data['order_Item_Flavor'], order_Sizes=form.cleaned_data['order_Sizes'])
            return redirect('continueorder')
    else:   
        form=customerOrder()
    
    return render(request, 'orderentry.html', {'form' : form})

def getCustomerInfo(request):
    form = customerInfo(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            orderentry.forms.customer_first_name = form.cleaned_data['customer_first_name']
            orderentry.forms.customer_last_name = form.cleaned_data['customer_last_name']
            orderentry.forms.shipping_address = form.cleaned_data['shipping_address']
            orderentry.forms.billing_address = form.cleaned_data['billing_address']
            return redirect('thankyou')

    else:
        form=customerInfo()
    
    return render(request, 'customerinfoentry.html', {'form' : form})

def thankYou(request):
    return render(request, 'thankyou.html')

def continueOrder(request):
    return render(request, 'customerinfoentry.html')