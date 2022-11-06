# from attr import fields
from types import MethodType
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Book, Author, BookInstance, Genre, Language
from django.views.generic import CreateView, DetailView, FormView
from .forms import DAForm, BuyerForm, SelectForm
from .scripts import generate_first_contact, generate_annual_review_with_supplier, generate_annual_review_no_supplier, da_type
from django.contrib.auth.decorators import login_required


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
        

        data_dir = {
            "da_type" : da_type["da_type"],
            "buyer_number" : buyer_form["buyer_number"].value(),
            "buyer_name" : buyer_form["buyer_name"].value(),
            "contact_name" : buyer_form["contact_name"].value(),
            "supplier_name" : da_form["supplier_name"].value(),
            "fins_required_1" : da_form["fins_required_1"].value(),
            "fins_required_2" : da_form["fins_required_2"].value(),
            "previous_contact" : da_form["previous_contact"].value(),
            "sender" : da_form["sender"].value()
        }

    #     # if DA1 selected context == x, elif DA2 CONTEXT == y
        if da_form.is_valid() and buyer_form.is_valid() and da_type.is_valid():
            print(da_type.cleaned_data["da_type"])
           
           
            #FIRST CONTACT
            if da_type.cleaned_data["da_type"] == "First Contact":
                # print(data_dir["da_type"]["First Contact"])
                context_2 = {
                    "da_script" : generate_first_contact(data_dir["buyer_number"], data_dir["buyer_name"], data_dir["contact_name"], data_dir["supplier_name"], data_dir["fins_required_1"],data_dir["fins_required_2"],data_dir["sender"])
                }
                return render(request, "DA_generator/script.html", context=context_2)
            
            elif  da_type.cleaned_data["da_type"] == "Annual Review w/ Supplier":
                # print(data_dir["da_type"]["First Contact"])
                context_2 = {
                    "da_script" : generate_annual_review_with_supplier(data_dir["buyer_number"], data_dir["buyer_name"], data_dir["contact_name"], data_dir["fins_required_1"],data_dir["fins_required_2"],data_dir["previous_contact"],data_dir["sender"])
                }
                return render(request, "DA_generator/script.html", context=context_2)
            
            elif  da_type.cleaned_data["da_type"] == "Annual Review no Supplier":
                context_2 = {
                    "da_script" : generate_annual_review_no_supplier(data_dir["buyer_number"], data_dir["buyer_name"], data_dir["contact_name"], data_dir["fins_required_1"],data_dir["fins_required_2"], data_dir["previous_contact"])
                }


                #if new buyer number save. probably query buyer number and if not .save()
                buyer_form.save()
                return render(request, "DA_generator/script.html", context=context_2)
            else:
                print("nao foi")
   

    # # num_instances_avail = BookInstance.objects.filter(status__exact="a").count()

    context = {
        # "num_books": num_books,
        # "num_instances": num_instances,
        # "num_instances_avail": num_instances_avail,
        "buyer_form": buyer_form,
        "da_form" : da_form,
        "da_type" : da_type,
    }



    return render(request, "DA_generator/index.html", context=context)




class BookCreate(CreateView): #book_form.html
    model = Book
    fields = "__all__"


class BookDetail(DetailView): 
    model = Book



def script_page(request):
    # use context items passed and use them as arguments in a function call
    
    return render(request, "DA_generator/script.html")


#create view for SCRIPT