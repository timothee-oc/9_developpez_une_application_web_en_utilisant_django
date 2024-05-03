from django import forms
from .models import Ticket, Review

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        exclude = ('user',)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ('user', 'ticket')