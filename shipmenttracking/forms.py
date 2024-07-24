from django import forms
from orderentry.models import orderInfo

class shipmentTrackForm (forms.Form):
    
    trackingCode = forms.UUIDField()
    class Meta:
        model=orderInfo