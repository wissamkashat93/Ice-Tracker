from django import forms
from ticketmanage.models import externalTicket

class ticketForm(forms.ModelForm):
    
    user_name = forms.CharField(max_length=30, label='Name')
    user_email = forms.CharField(max_length=30, label='Email')
    ticket_creation_date = externalTicket.ticket_creation_date
    subject = forms.CharField(max_length=40, label='Subject')
    description = forms.TextInput()

    class Meta:
        model = externalTicket
        fields = ('user_name','user_email','ticket_creation_date', 'subject','description')