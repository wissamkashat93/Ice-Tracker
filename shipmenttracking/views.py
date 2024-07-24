from django.shortcuts import render
from django.http import HttpResponse
import shipmenttracking
from orderentry.models import orderInfo
from shipmenttracking.forms import shipmentTrackForm 

def getShipmentCode(request):
    form = shipmentTrackForm(request.GET)
    if request.method == 'GET':
        if form.is_valid():
            order = orderInfo.objects.filter(id=form.cleaned_data['trackingCode'])
            return render(request, 'shipmenttracking.html', {'order' : order} )
    else:
        form = shipmentTrackForm()
    
    return render(request, 'shipmenttracking.html', {'form' : form})