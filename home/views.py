from django.shortcuts import render
from django.http import HttpResponse
from orderentry.models import orderInfo

def index(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def getCustomerInfo(request):
    order_info_list = orderInfo.objects.all()
    return render(request, 'customerinfoentry.html', {'order_info_list': order_info_list})

