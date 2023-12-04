# from attr import fields
from types import MethodType
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, DetailView, FormView
from .forms import DAForm, BuyerForm, SelectForm
from .scripts import generate_first_contact, generate_annual_review_with_supplier, generate_annual_review_no_supplier, da_type, generate_NNP_info,generate_claims_WD, generate_header
from django.contrib.auth.decorators import login_required
from .models import BuyerDB
from django.db.models import Q
from django.contrib import messages
from django.core.exceptions import *
from django.http import HttpResponse
from . models import BuyerDB
from django import template

# Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException, ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
import time


user = "pedro.peres@atradius.com"
password = "Aupper1289*"

#-----------------------------------CONSTANTS--------------------------------------------------#

WEBSITE = "https://illiondirect.com.au/Integate/Landing.mvc?upid=6381337274462243642118621850&referrer=Login"

LOGIN = user
PASS = password

LOGIN_FIELD = '//*[@id="txtEmail"]'
PASSWORD_FIELD = '//*[@id="txtPassword"]'


COUNTRY_BUTTOM = '/html/body/div[1]/div[1]/div[1]/div[1]/div/div[2]/a/span[1]'
COUNTRY_FIELD = '/html/body/div[4]/div/input'
COUNTRY_FIELD_ID = 's2id_autogen1_search'

SEARCH_FIELD = '//*[@id="txbSearchKeyword"]'
BUYER_FIELD =' //*[@id="tabBureau"]/tbody/tr[1]/td[2]/p[1]/a/b'
BUYER_FIELD_2 = '//*[@id="tabBureau"]/tbody/tr[1]/td[2]/p[1]/a'
BUYER_FIELD_3 = '/html/body/div[1]/div[2]/div[2]/table[1]/tbody/tr[1]/td[2]/p[1]/a'
SECOND_BUYER = '/html/body/div[1]/div[2]/div[2]/table[1]/tbody/tr[3]/td[2]/p[1]/a'



ACN_FIELD ='/html/body/div[1]/div[2]/div[2]/table[1]/tbody/tr[1]/td[4]/p[4]'
NCN_FIELD = '/html/body/div[1]/div[2]/div[2]/table[1]/tbody/tr[1]/td[4]/p[4]'

COMPANY_FINANCIALS_BUTTOM = '/html/body/div[1]/div[2]/div[3]/div/div[3]/div[4]/a[1]/div'

FINS_2022 = '/html/body/div[1]/div[2]/div[3]/div/div[4]/form/table/tbody/tr[3]/td/div[2]/div[2]/div[1]/div[1]/div[2]/div[3]'
FINS_2023 = '//*[@id="2023"]'

DB_BUTTON = '//*[@id="content_mid"]/div[3]/div/div[3]/div[1]/a[1]/div'

DB_BUTTON_AFTER_FINS = '/html/body/div[1]/div[2]/div[3]/div/div[3]/div[1]/a[1]/div'

INVESTIGATION_NO = '/html/body/div[1]/div[2]/div[3]/div/div[4]/form/table/tbody/tr[4]/td/div[2]/table/tbody/tr[2]/td/div/div/p/input[2]'

INVESTIGATION_PROCESSING_TIME = '/html/body/div[1]/div[2]/div[3]/div/div[4]/form/table/tbody/tr[4]/td/div[2]/table/tbody/tr[2]/td/div/div/input[1]'

INVESTIGATION_EMAIL_COPY = '/html/body/div[1]/div[2]/div[3]/div/div[4]/form/table/tbody/tr[4]/td/div[2]/table/tbody/tr[3]/td/input[1]'

INVESTIGATION_BUTTOM = '/html/body/div[1]/div[4]/div[6]/div[2]/div[1]/p[2]/input'

SMALL_REPORT = '/html/body/div[1]/div[2]/div[3]/div/div[3]/div[1]/a[5]/div'

TRANS_REF_FIELD = '//*[@id="TransactionReference"]'

INTERNAL_REF_FIELD = '//*[@id="SubscriberReferenceId"]'

ENQUIRY_TYPE_FIELD = '//*[@id="Fields_1__Value"]'

TEAM_FIELD = '//*[@id="Fields_2__Value"]'

FINS_TEXT = '//*[@id="vapmsg"]/p'

FINS_TEXT_ALT = '//*[@id="vapmsgHolding"]/p'

PURCHASE_BUTTON = '//*[@id="SubmitOrder"]'

SEGUNDOS = 6

FINS_MESSAGE_AVAILABLE = "This financial report is available. To view please proceed with purchasing report."

FINS_MESSAGE_UNAVAILABLE = "Documents for this financial year are not available on file. Please proceed to Document List to order available ASIC documents"

FINS_MESSAGE_UNAVAILABLE_2 = "Documents for this financial year are not available on file. Please proceed to Document List to order available ASIC documents"

FINS_ALREADY_PURCHASED = "You have already purchased this report. Any additional on-file documents that get added for this financial year will automatically be added to this report. Click here to view."

FINS_ALREADY_PURCHASED_2 = "You have already purchased this report. Any additional on-file documents that get added for this financial year will automatically be added to this report. Click here to view."

#----------------------------------------------------------------Illion Scraper CLASS ------------------------------------------------------
class IllionScraper:

    def __init__(self):
        #innitiates IllionScraper. Update ChromeDriver path when new version of Chrome comes out.
        chrome_driver_path = "E:\Documentos\Development\chromedriver.exe"

        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
        self.driver.maximize_window()
      

        self.action_chains = ActionChains(self.driver)

    def scroll_up(self):
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
    
#----------------------------------loging in and searching buyer--------------------------------------------#

    def log_in(self):
        #Launches website and logs into Illion with user and password
        try:
            self.driver.get(WEBSITE)
            time.sleep(3)
            login_field = self.driver.find_element_by_xpath(LOGIN_FIELD)
            login_field.send_keys(user)
            password_field = self.driver.find_element_by_xpath(PASSWORD_FIELD)
            password_field.send_keys(password)
            time.sleep(1)
            password_field.submit()
            time.sleep(5)
        except NoSuchElementException or StaleElementReferenceException:
            print(" no login or pass field")

    def select_country(self, country):
        try:
            country_buttom = self.driver.find_element_by_xpath(COUNTRY_BUTTOM)
            country_buttom.click()
            country_field = self.driver.find_element_by_xpath(COUNTRY_FIELD)
            country_field.click()
            if country == "NZL" or "New Zealand":
                country_field.send_keys("new")
                country_field.send_keys(Keys.RETURN)
            else:
                country_field.send_keys("aus")
                country_field.send_keys(Keys.RETURN)
        except NoSuchElementException or StaleElementReferenceException:
            print(" no country field")
        except ElementClickInterceptedException:  #EXCEPTION IS WAITING 3 SECONDS AND TRYING AGAIN IF CLICK INTERCEPTED
            print("click intercepted")
            time.sleep(10)
            country_buttom = self.driver.find_element_by_xpath(COUNTRY_BUTTOM)
            country_buttom.click()
            country_field = self.driver.find_element_by_xpath(COUNTRY_FIELD)
            country_field.click()
            if country == "NZL"or "New Zealand":
                country_field.send_keys("new")
                country_field.send_keys(Keys.RETURN)
            else:
                country_field.send_keys("aus")
                country_field.send_keys(Keys.RETURN)
        except StaleElementReferenceException or ElementClickInterceptedException:
            time.sleep(3)
            country_buttom = self.driver.find_element_by_xpath(COUNTRY_BUTTOM)
            country_buttom.click()
            country_field = self.driver.find_element_by_xpath(COUNTRY_FIELD)
            country_field.click()
            if country == "NZL"or "New Zealand":
                country_field.send_keys("new")
                country_field.send_keys(Keys.RETURN)
            else:
                country_field.send_keys("aus")
                country_field.send_keys(Keys.RETURN)


    def search_buyer(self, business_num):
        try:
            search_field = self.driver.find_element_by_xpath(SEARCH_FIELD)
            search_field.send_keys(business_num) #leader computers
            time.sleep(1)
            search_field.send_keys(Keys.RETURN)
            # print(buyer)
        except NoSuchElementException or StaleElementReferenceException:
            print(" no search field")
            time.sleep(5)

    def confirm_acn(self,business_num):
        #CHECKS IF REALLY ACN NUMBER OR DOCUMENT NUMBER WITH SAME VALUE AS ACN
        try:
            acn_field = self.driver.find_element_by_xpath(ACN_FIELD)
            acn_joined = acn_field.text.replace(" ", "")
            print(acn_joined)
            print(business_num)
            if business_num == (acn_joined):
                return True
            else:
                return False
        except NoSuchElementException:
            pass


    def click_buyer(self):
        try:
            buyer_field = self.driver.find_element_by_xpath(BUYER_FIELD)
            buyer_field.click()
        except NoSuchElementException or StaleElementReferenceException:
            try:
                buyer_field = self.driver.find_element_by_xpath(BUYER_FIELD_3)
                buyer_field.click()
            except NoSuchElementException or StaleElementReferenceException:
                print("not found")
                pass

    def click_second_buyer(self):
        try:
            buyer_field = self.driver.find_element_by_xpath(SECOND_BUYER)
            buyer_field.click()
        except NoSuchElementException or StaleElementReferenceException:
            
            print("second buyer non existant")


#------Ordering Reports-------------------------------------------------

    def click_DB_REPORT(self):
        try:
            db_button = self.driver.find_element_by_xpath(DB_BUTTON_AFTER_FINS)
            db_button.click()
        except ElementClickInterceptedException:
            time.sleep(5)
            db_button = self.driver.find_element_by_xpath(DB_BUTTON_AFTER_FINS)
            db_button.click()
        except NoSuchElementException or StaleElementReferenceException:
            print(" no DB report button found")
            pass
       

    def click_small_report(self):
        try:
            db_button = self.driver.find_element_by_xpath(SMALL_REPORT)
            db_button.click()
        except NoSuchElementException or StaleElementReferenceException:
            print(" no Small report button found")
            pass
        

    def input_report_data(self,buyer_number,buyer_name):
        try:
            trans_ref_field = self.driver.find_element_by_xpath(TRANS_REF_FIELD)
            trans_ref_field.click()
            trans_ref_field.send_keys("Illion searcher")
            trans_ref_field.send_keys(Keys.TAB)
            internal_ref_field = self.driver.find_element_by_xpath(INTERNAL_REF_FIELD)
            internal_ref_field.send_keys(f"{buyer_number}_buinf101a_{buyer_name[0:3]}_pp")
            enquiry_type = self.driver.find_element_by_xpath(ENQUIRY_TYPE_FIELD)
            enquiry_type.send_keys("ot")
            team_field = self.driver.find_element_by_xpath(TEAM_FIELD)
            team_field.send_keys("r")
        except NoSuchElementException or StaleElementReferenceException:
            print(" problem with input fields")
        except ElementNotInteractableException:
            print("This report is not available in Illion")
            with open('buyers_list.txt', 'a') as f:
                f.write(f'{buyer}, This report is not available in Illion')
                f.write("\n")

    def check_for_investigation(self):
        try:
            self.driver.find_element_by_xpath(INVESTIGATION_NO)
            
        except NoSuchElementException: 
            return False
        return True
    
    def check_for_investigation_buttom(self):
        try:
            self.driver.find_element_by_xpath(INVESTIGATION_BUTTOM)
        except NoSuchElementException:
            return False
        return True
    
    def click_investigation_buttom(self):
        buttom = self.driver.find_element_by_xpath(INVESTIGATION_BUTTOM)
        buttom.click()

    def investigation_order(self):
        investigation_options_no = self.driver.find_element_by_xpath(INVESTIGATION_NO)
        investigation_options_no.click()
        processing_time_5 = self.driver.find_element_by_xpath(INVESTIGATION_PROCESSING_TIME)
        processing_time_5.click()
        email_copy = self.driver.find_element_by_xpath(INVESTIGATION_EMAIL_COPY)
        email_copy.click()

    def buy_report(self,buyer):
        try:
            purchase_report = self.driver.find_element_by_xpath(PURCHASE_BUTTON)
            purchase_report.click()
            self.write_report_ordered(buyer)
        except NoSuchElementException or StaleElementReferenceException:
            print(" problem with Buy Button")
            





#----------------------------------------------------------------Illion Scraper CLASS END------------------------------------------------------
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


def scrap(request):
        #innitiates IllionScraper. Update ChromeDriver path when new version of Chrome comes out.
        chrome_driver_path = "E:\Documentos\Development\chromedriver.exe"

        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
        driver.maximize_window()
        return HttpResponse(request, "DA_generator/scrap.html")

register = template.Library()


def order_DB(request, buyer_country, business_number,buyer_number,buyer_name):
        bot = IllionScraper()
        bot.log_in()
        time.sleep(2)
        bot.select_country(buyer_country)
        bot.search_buyer(business_number)   
        if bot.confirm_acn(business_number):  #CHECKS IF REALLY ACN NUMBER OR DOCUMENT NUMBER WITH SAME VALUE AS ACN
            bot.click_buyer(buyer)
            bot.write_buyer_name(buyer)
            bot.click_DB_REPORT() 
            bot.input_report_data(buyer_number, buyer_name)
            if bot.check_for_investigation():
                bot.investigation_order()
            else:
                pass
            # bot.buy_report(buyer)                         #TURNS BUYING FUNCTION ON/OFF
            # if bot.check_for_investigation_buttom():
            #     time.sleep(5)
            #     bot.click_investigation_buttom()        
            # else:
            #     pass
            # time.sleep(5)
            
        else:
            bot.click_second_buyer()
            bot.click_DB_REPORT() 
            bot.input_report_data(buyer)
            if bot.check_for_investigation():
                bot.investigation_order()
            else:
                pass
            # bot.buy_report(buyer)                         #TURNS BUYING FUNCTION ON/OFF
            # if bot.check_for_investigation_buttom():
            #     time.sleep(5)
            #     bot.click_investigation_buttom()        
            # else:
            #     pass
            #     time.sleep(5)
            

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
    
    