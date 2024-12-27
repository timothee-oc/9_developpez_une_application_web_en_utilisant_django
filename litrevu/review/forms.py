from django import forms
from . import models


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        exclude = ("user",)
        widgets = {
            "title": forms.TextInput(attrs={"class": "d-block w-75 m-auto"}),
            "description": forms.Textarea(attrs={"class": "d-block w-75 m-auto"}),
            "image": forms.FileInput(attrs={"class": "d-block w-75 m-auto"}),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        exclude = ("user", "ticket")
        widgets = {
            "headline": forms.TextInput(attrs={"class": "d-block w-75 m-auto"}),
            "rating": forms.NumberInput(attrs={"class": "d-block w-75 m-auto"}),
            "body": forms.Textarea(attrs={"class": "d-block w-75 m-auto"}),
        }
