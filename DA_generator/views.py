# from attr import fields
from types import MethodType
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import CreateView, DetailView, FormView
from .forms import DAForm, BuyerForm, SelectForm
from .scripts import generate_first_contact, generate_annual_review_with_supplier, generate_annual_review_no_supplier, da_type, generate_NNP_info,generate_claims_WD, generate_header
from django.contrib.auth.decorators import login_required
from .models import BuyerDB
from django.db.models import Q
from django.contrib import messages
from django.core.exceptions import *
from django.http import HttpResponse
import time
from illion_scraper import IllionScraper

# Create your views here.

@login_required
def index(request):
    da_form = DAForm()
    buyer_form = BuyerForm()
    da_type = SelectForm()
    

    if request.method == "POST":
        
        da_type = SelectForm(request.POST)
        da_form = DAForm(request.POST)
        buyer_form = BuyerForm(request.POST)
        
        buyer = BuyerDB.objects.get(buyer_number= buyer_form["buyer_number"].value())
        buyer_name = BuyerDB.objects.get(buyer_number= buyer_form["buyer_number"].value())

        data_dir = {
            "da_type" : da_type["da_type"],
            "buyer_number" : buyer.buyer_number,
            "buyer_number_1" : buyer_form["buyer_name"].value(),
            "buyer_name" : buyer.buyer_name,                           
            "contact_name" : da_form["contact_name"].value(),
            "customer_name" : da_form["customer_name"].value(),
            "fins_required_1" : da_form["fins_required_1"].value(),
            "fins_required_2" : da_form["fins_required_2"].value(),
            "previous_contact" : da_form["previous_contact"].value(),
            "sender" : da_form["sender"].value()
        }

    #     # if DA1 selected context == x, elif DA2 CONTEXT == y
        if da_form.is_valid() and buyer_form.is_valid() and da_type.is_valid():
            print(da_type.cleaned_data["da_type"])
           
            #FIRST CONTACT
            if da_type.cleaned_data["da_type"] == "5 - DA First Contact":
                # print(data_dir["da_type"]["First Contact"])
                
                context_2 = {
                    "da_header" : generate_header(data_dir["buyer_number"], data_dir["buyer_name"]),
                    "da_script" : generate_first_contact(data_dir["buyer_number"], data_dir["buyer_name"], data_dir["contact_name"], data_dir["customer_name"], data_dir["fins_required_1"],data_dir["fins_required_2"],data_dir["sender"])
                }
                buyer_form.save()
                return render(request, "DA_generator/script.html", context=context_2)
            
            elif  da_type.cleaned_data["da_type"] == "6 - DA Annual Review":
                # print(data_dir["da_type"]["First Contact"])
                context_2 = {
                    "da_script" : generate_annual_review_with_supplier(data_dir["buyer_number"], data_dir["buyer_name"], data_dir["contact_name"], data_dir["fins_required_1"],data_dir["fins_required_2"],data_dir["previous_contact"],data_dir["sender"])
                }
                return render(request, "DA_generator/script.html", context=context_2)
            
            elif  da_type.cleaned_data["da_type"] == "7 - DA Annual Review no Supplier":
                context_2 = {
                    "da_script" : generate_annual_review_no_supplier(data_dir["buyer_number"], data_dir["buyer_name"], data_dir["contact_name"], data_dir["fins_required_1"],data_dir["fins_required_2"], data_dir["previous_contact"])
                }

                #if new buyer number save. probably query buyer number and if not .save()
                buyer_form.save()
                return render(request, "DA_generator/script.html", context=context_2)
            
            elif da_type.cleaned_data["da_type"] == "2 - NNP WD":
                context_2 = {
                    "da_script" : generate_NNP_info(data_dir["buyer_number"], data_dir["buyer_name"], data_dir["contact_name"], data_dir["customer_name"])
                }
                buyer_form.save()
                return render(request,"DA_generator/script.html", context=context_2)
            
            

            elif da_type.cleaned_data["da_type"] == "3 - Claims WD":
                context_2 = {
                    "da_script" : generate_claims_WD(data_dir["buyer_number"], data_dir["buyer_name"], data_dir["contact_name"], data_dir["customer_name"])
                }
                buyer_form.save()
                return render(request,"DA_generator/script.html", context=context_2)


            elif da_type.cleaned_data["da_type"] == "1 - NNP Info":
                try:
                    context_2 = {
                        "da_script" : generate_NNP_info(data_dir["buyer_number"], data_dir["buyer_name"], data_dir["contact_name"], data_dir["customer_name"])
                    }
                    buyer_form.save()
                    return render(request,"DA_generator/script.html", context=context_2)
                
                except BuyerDB.buyer_number.DoesNotExist or ObjectDoesNotExist:
                    context_2 = {
                        "da_script" : generate_NNP_info(data_dir["buyer_number_1"], data_dir["buyer_name"], data_dir["contact_name"], data_dir["customer_name"])
                    }
                    buyer_form.save()
                    return render(request,"DA_generator/script.html", context=context_2)
            else:
                print("nao foi")
    context = {

        "buyer_form": buyer_form,
        "da_form" : da_form,
        "da_type" : da_type,
    }



    return render(request, "DA_generator/index.html", context=context)

def script_page(request):
    # use context items passed and use them as arguments in a function call
    
    return render(request, "DA_generator/script.html")


#create view for SCRIPT

def order_DB(request,buyer_acn,buyer_country):
        bot = IllionScraper()
        bot.log_in()
        time.sleep(2)
        bot.select_country(buyer_country)
        bot.search_buyer(buyer_acn)   
        if bot.confirm_acn(buyer):  #CHECKS IF REALLY ACN NUMBER OR DOCUMENT NUMBER WITH SAME VALUE AS ACN
            bot.click_buyer(buyer)
            bot.write_buyer_name(buyer)
            bot.click_DB_REPORT() 
            bot.input_report_data(buyer)
            if bot.check_for_investigation():
                bot.investigation_order()
            else:
                pass
            bot.buy_report(buyer)                         #TURNS BUYING FUNCTION ON/OFF
            if bot.check_for_investigation_buttom():
                time.sleep(5)
                bot.click_investigation_buttom()        
            else:
                pass
            time.sleep(5)
            
        else:
            bot.click_second_buyer(buyer)
            bot.click_DB_REPORT() 
            bot.input_report_data(buyer)
            if bot.check_for_investigation():
                bot.investigation_order()
            else:
                pass
            bot.buy_report(buyer)                         #TURNS BUYING FUNCTION ON/OFF
            if bot.check_for_investigation_buttom():
                time.sleep(5)
                bot.click_investigation_buttom()        
            else:
                pass
                time.sleep(5)
            

def all_buyers(request):
    if request.method == "POST":
        searched = request.POST['searched']
        buyers = BuyerDB.objects.filter(Q(buyer_number__contains= searched) | Q(buyer_name__contains=searched) | Q(business_number__contains=searched))

        buyer_list = BuyerDB.objects.all()

        return render(request, "DA_generator/buyer_list.html", 
                    {"searched" : searched, "buyers" : buyers}
                   )
    else:
        buyer_list = BuyerDB.objects.all()

        return render(request, "DA_generator/buyer_list.html", 
                    {"buyer_list" : buyer_list}
                   )
    
    
    def simple(request):
        print("testing")
        return HttpResponse(""" """)
    
    