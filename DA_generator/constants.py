from illion_login import user, password

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