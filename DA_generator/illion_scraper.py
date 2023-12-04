from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException, ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from constants import *
import time

#-----------------------------------SCRAPER--------------------------------------------------#

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

    def select_country(self, buyer):
        try:
            country_buttom = self.driver.find_element_by_xpath(COUNTRY_BUTTOM)
            country_buttom.click()
            country_field = self.driver.find_element_by_xpath(COUNTRY_FIELD)
            country_field.click()
            if buyer.country == "NZL":
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
            if buyer.country == "NZL":
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
            if buyer.country == "NZL":
                country_field.send_keys("new")
                country_field.send_keys(Keys.RETURN)
            else:
                country_field.send_keys("aus")
                country_field.send_keys(Keys.RETURN)


    def search_buyer(self, buyer):
        try:
            search_field = self.driver.find_element_by_xpath(SEARCH_FIELD)
            search_field.send_keys(buyer.business_num) #leader computers
            time.sleep(1)
            search_field.send_keys(Keys.RETURN)
            # print(buyer)
        except NoSuchElementException or StaleElementReferenceException:
            print(" no search field")
            time.sleep(5)

    def confirm_acn(self,buyer):
        #CHECKS IF REALLY ACN NUMBER OR DOCUMENT NUMBER WITH SAME VALUE AS ACN
        try:
            acn_field = self.driver.find_element_by_xpath(ACN_FIELD)
            acn_joined = acn_field.text.replace(" ", "")
            print(acn_joined)
            print(buyer.business_num)
            if buyer.business_num == (acn_joined):
                return True
            else:
                return False
        except NoSuchElementException:
            pass


    def click_buyer(self,buyer):
        try:
            buyer_field = self.driver.find_element_by_xpath(BUYER_FIELD)
            buyer_field.click()
        except NoSuchElementException or StaleElementReferenceException:
            try:
                buyer_field = self.driver.find_element_by_xpath(BUYER_FIELD_3)
                buyer_field.click()
            except NoSuchElementException or StaleElementReferenceException:
                self.write_buyer_not_found(buyer)
                pass

    def click_second_buyer(self, buyer):
        try:
            buyer_field = self.driver.find_element_by_xpath(SECOND_BUYER)
            buyer_field.click()
        except NoSuchElementException or StaleElementReferenceException:
            self.write_buyer_not_found(buyer)
            print("second buyer non existant")






    

            


#----------------------------------------Ordering Reports-------------------------------------------------

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
        

    def input_report_data(self,buyer):
        try:
            trans_ref_field = self.driver.find_element_by_xpath(TRANS_REF_FIELD)
            trans_ref_field.click()
            trans_ref_field.send_keys("Illion searcher")
            trans_ref_field.send_keys(Keys.TAB)
            internal_ref_field = self.driver.find_element_by_xpath(INTERNAL_REF_FIELD)
            internal_ref_field.send_keys(f"{buyer.buyer_num}_buinf101a_{buyer.name[0:3]}_pp")
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
            
#------------------------------------WRITING FUNCTIONS-------------------------------------------------------------#

    def write_result(self, buyer):
        with open('buyers_list.txt', 'a') as f:
            f.write(f'{buyer} - Latest Fins available in Illion')
            f.write("\n")

    def write_not_available(self, year):
        with open('buyers_list.txt', 'a') as f:
            f.write(f'{year}  Fins NOT available in Illion')
            f.write("\n")

    def write_error_message(self, buyer):
        with open('buyers_list.txt', 'a') as f:
            f.write(f'{buyer} - Error while searching for buyer, please try manually')
            f.write("\n")

    def write_buyer_not_found(self,buyer):
        with open('buyers_list.txt', 'a') as f:
            f.write(f'{buyer} - Error while searching for buyer, please try manually')
            f.write("\n")

    def write_no_fins_available(self):
        with open('buyers_list.txt', 'a') as f:
            f.write('No fins available for buyer')
            f.write("\n")

    def write_purchased(self,year):
        with open('buyers_list.txt', 'a') as f:
            f.write(f'{year}Fins already purchased')
            f.write("\n")

    def write_final_results(self,number_of_buyers, total_time_minutes, current_time):
        with open('buyers_list.txt', 'a') as f:
            f.write(f'Script concluded {current_time}, {number_of_buyers} Buyers searched in {total_time_minutes} minutes. ')
            f.write("\n")

    def write_buyer_name(self, buyer):
        with open('buyers_list.txt', 'a') as f:
            f.write(f'{buyer.name}')
            f.write("\n")
    def write_fins_available(self, year):
        with open('buyers_list.txt', 'a') as f:
            f.write(f'{year} financials available to order')
            f.write("\n")

    def write_report_ordered(self, buyer):
        if buyer.report_type == "B":
            report = "D&B Report"
        else:
            report = "Risk of Late Payment"
        with open('buyers_list.txt', 'a') as f:
            f.write(f'{report}, Report Ordered')
            f.write("\n")
            f.write("\n")


    def write_report_unavailable(self, buyer):
        with open('buyers_list.txt', 'a') as f:
            f.write(f'{buyer}, This report is not available in Illion')
            f.write("\n")







    # def get_info(self, p_number):   #add date from last update on sheet as variable
    #     """Opens process and gets last update"""
    #     try:
    #         self.processos.append(p_number)
    #         self.driver.get(WEBSITE)
    #         time.sleep(3)
    #         processo = self.driver.find_element_by_xpath(PROCESS_FIELD)
    #         processo.clear()
    #         processo.send_keys(p_number)
    #         time.sleep(1)
    #         processo.submit()
    #         time.sleep(SEGUNDOS)
    #         titulo_processo = self.driver.find_element_by_xpath(TITULO_PROCESSO)
    #         titulo_processo.click()
    #         time.sleep(6)
    #         self.ultimas_mov = self.driver.find_elements_by_id("conteudo_movimentacoes")
    #         return self.ultimas_mov

    #     except NoSuchElementException or StaleElementReferenceException:
    #         self.andamentos.append(f"Erro ao buscar ultima atualizacao do processo {p_number}")






            #PEGA MOVIMENTACOES DIVIDE EM ITENS INDIVIDUAIS E ADICIONA A UMA LISTA DE ANDAMENTOS
            # for mov in ultimas_mov:
            #     andamentos = []
            #     lista_andamentos = []
            #     dict_processos = {}
            #     andamentos.append(mov.text)
            #
            #     nova_lista = andamentos[0].split("\n")
            #     ultima_data = nova_lista[0].split(" -")



                # #pega e formata datas. passar para classe
                # for andamento in nova_lista:
                #     data_andamento = andamento.split(" -")[0]
                #     data_andamento2 = data_andamento.split("/")
                #     dia_andamento = int(data_andamento2[0])
                #     mes_andamento = int(data_andamento2[1])
                #     ano_andamento = int(data_andamento2[2])
                #     data_andamento_formatada = datetime.datetime(ano_andamento, mes_andamento, dia_andamento)
                #
                #     #transformar funcao(p_number, ultima atualizacao
                #     if data_andamento_formatada > datetime.datetime(2021,1,1):
                #         print("data maior")
                #         lista_andamentos.append(andamento)
                #         # lista.where() para python
                #
                #         dict_processos[p_number] = lista_andamentos
                #
                #     else:
                #         pass
                #
                # print(dict_processos)


                        #adiciona andamento a lista para
                    # else:
                        #escreve ultima data de andamento




                #FORMATA DATA DE CADA MOVIMENTACAO PARA ELA PODER SER COMPARADA COM A DATA EM QUE O PROGRAMA RODOU PELA ULTIMA VEZ

                # data = ultima_data[0]
                # # print(nova_lista)
                # calendar = data.split("/")
                # day = int(calendar[0])
                # month = int(calendar[1])
                # year = int(calendar[2])
                #
                # ultima_data_formatada = datetime.datetime(year, month, day)
                # date2 = datetime.datetime(1989, 5,28)
                #
                #
                # if ultima_data_formatada > date2:
                #     print("data maior")

                # for item in nova_lista:
                #      if item.split(" -")[0] > data:
                #          print("cu")
                #         #identificar a atualizacao nova e adicionar ela em uma lista pra enviar por email



            #pega movs do processo e cria dicionario com numero de processo como key e lista de processos como value
            # try:
            #     #append content of the div to a list and splits into bigger list
            #     for mov in ultimas_mov:
            #
            #         self.lista_andamentos.append(mov.text)
            #
            #     self.processos_dict = dict(zip(self.processos, self.lista_andamentos))
            #     print(len(self.lista_andamentos))
            #     # print(self.processos_dict)
            #     print(self.processos_dict)


            #     #USAR SPLIT SOMENTE NA HORA DE ESCREVER
            #
            # except IndexError:
            #     print(f"Falha ao pesquisar processo {p_number}")
            #     self.numero_andamentos.append(0)




            # ultima_mov = self.driver.find_element_by_xpath(ULTIMA_MOV).text
            # self.andamentos.append(ultima_mov)
            # print(ultima_mov)
            # time.sleep(3)




# Comparar len de cada lista de andamentos. se valor for igual nao houveram novos andamentos. se valor for diferente novos andamentos realizados
# quantidade de novos andamentos = len(nova) - len(antiga)





