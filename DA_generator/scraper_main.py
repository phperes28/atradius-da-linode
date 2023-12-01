#---------------------                                              IMPORTS                            ---------------------#
from illion_scraper import IllionScraper
import time


#------------------------------------------------------CHECKING FOR FINS AND REPORT ORDERING FUNCTIONS -------------------------------------------------------------

def order_DB(buyer_acn,buyer_country):
    bot = IllionScraper()
    bot.log_in()
    num = 1
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
        
    


end = time.time()
total_time = (end - current_time) 
total_time_minutes = total_time/60
current_time = time.time()

print(f"Processo concluido em {current_time} em {total_time_minutes} minutos")
# bot.write_final_results(number_of_buyers, total_time_minutes, current_time)
# winsound.Beep(freq, duration)



 














