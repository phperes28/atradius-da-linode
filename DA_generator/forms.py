from django.forms import ModelForm
from DA_generator.models import BuyerDB, BuyerForm, DAInfo
from django import forms
from .scripts import da_type


class BuyerForm(ModelForm):
    class Meta:
        model = BuyerForm
        fields = "__all__"

        widgets = {
            "buyer_number" : forms.TextInput(attrs={"class": "form-control"}),
            "buyer_name" : forms.TextInput(attrs={"class": "form-control"}),
            "contact_name" : forms.TextInput(attrs={"class": "form-control"}),
            "contact_number" : forms.TextInput(attrs={"class": "form-control"}),
            "contact_email" : forms.TextInput(attrs={"class": "form-control"}),
            
        }


class DAForm(ModelForm):
    class Meta:
        model = DAInfo
        widgets = {
            "customer_name" : forms.TextInput(attrs={"class": "form-control"}),
            "fins_required_1" : forms.TextInput(attrs={"class": "form-control"}),
            "fins_required_2" : forms.TextInput(attrs={"class": "form-control"}),
            "previous_contact" : forms.TextInput(attrs={"class": "form-control"}),
            "sender" : forms.TextInput(attrs={"class": "form-control"}),
            

        }
        

        fields = "__all__"

class SelectForm(forms.Form):

    da_type = forms.ChoiceField(label='Select type  ', widget=forms.Select(), choices=da_type)

   