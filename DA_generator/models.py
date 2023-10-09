from audioop import reverse
from django.db import models
from django.urls import reverse
from .scripts import da_type

# Create your models here.



import uuid




class BuyerForm(models.Model):
    
    buyer_number = models.IntegerField(null=True, blank=True)
    buyer_name = models.CharField(max_length=100, null=True, blank=True)
    customer_name = models.CharField(max_length=100, null=True, blank=True)
    # contact_name = models.CharField(max_length=50, null=True, blank=True)
    # contact_number = models.IntegerField(null=True, blank=True)
    # contact_email = models.EmailField(null=True, blank=True)
    

    def __str__(self):
        return f'{self.buyer_name} - {self.buyer_number}'


class DAInfo(models.Model):
#    buyer = models.ForeignKey("Buyer", on_delete=models.SET_NULL, null=True)
   fins_required_1 = models.CharField(max_length=100, null=True, blank=True)
   fins_required_2 = models.CharField(max_length=100, null=True, blank=True)
   previous_contact = models.CharField(max_length=100, null=True, blank=True)
   sender = models.CharField(max_length=100, null=True, blank=True)


class SRInfo(models.Model):
    parent_company = models.CharField(max_length=100, null=True, blank=True)
    ownership_percentage = models.IntegerField(null=True, blank=True)


class BuyerDB(models.Model):
     
     buyer_number = models.IntegerField(null=True, blank=True)
     buyer_name = models.CharField(max_length=100, null=True, blank=True)
     business_number = models.IntegerField(null=True, blank=True)
     buyer_country = models.CharField(max_length=100, null=True, blank=True)

     def __str__(self):
            return f"{self.buyer_name}, BN:{self.buyer_number}, ACN:{self.business_number}, Country:{self.buyer_country}"
     def __eq__(self, other):
            return (self.buyer_num) == (other.buyer_num)
     def __hash__(self):
        return super().__hash__()
     
        
        
        