

#Buyer list acquired by converting excel spreadsheet to json using: https://products.aspose.app/cells/conversion/excel-to-json

buyer_json = [
 

 {
  "NAME": "GOLDENGROVE BUILDING GROUP PTY LTD",
  "BN": 95795860,
  "REPORT_TYPE": "S",
  "A.C.N": "133890623",
  "Country": "Australia"
 },
 {
  "NAME": "MELCHOR MEP PTY LTD",
  "BN": 52281446,
  "REPORT_TYPE": "S",
  "A.C.N": "610067546",
  "Country": "Australia"
 },
 {
  "NAME": "MS7 ENTERPRISES PTY LTD",
  "BN": 48088325,
  "REPORT_TYPE": "S",
  "A.C.N": "083192358",
  "Country": "Australia"
 },
 {
  "NAME": "PRETTY SALLY HOLDINGS PTY LTD",
  "BN": 19410318,
  "REPORT_TYPE": "S",
  "A.C.N": "111744382",
  "Country": "Australia"
 },
 {
  "NAME": "ADCO NOMINEES PTY LTD",
  "BN": 22653808,
  "REPORT_TYPE": "S",
  "A.C.N": "128513191",
  "Country": "Australia"
 },
 {
  "NAME": "AXIS PLUMBING PTY. LTD.",
  "BN": 16243343,
  "REPORT_TYPE": "S",
  "A.C.N": "063032048",
  "Country": "Australia"
 },
 {
  "NAME": "CLASSIC BUILDERS GROUP LIMITED",
  "BN": 22128331,
  "REPORT_TYPE": "S",
  "A.C.N": "004074119",
  "Country": "NZL"
 },
 {
  "NAME": "BBC (SA) HOLDINGS PTY LTD",
  "BN": 22041452,
  "REPORT_TYPE": "S",
  "A.C.N": "614015093",
  "Country": "Australia"
 }
]
# Iterates json list and create a Buyer class object for every iteration.

buyer_list = []

for list_item in buyer_json:
  
    buyer = Buyer(list_item["NAME"], list_item["BN"], list_item["A.C.N"], list_item["Country"], list_item["REPORT_TYPE"])
    if buyer not in buyer_list:
      buyer_list.append(buyer)
      print(buyer)


    class Buyer:
        def __init__(self,name, buyer_num, business_num, country):
            self.name = name
            self.buyer_num = buyer_num
            self.business_num = business_num
            self.country = country
           
        
        def __str__(self):
            return f"{self.name}, BN:{self.buyer_num}, ACN:{self.business_num}, Country:{self.country} Report Type:{self.report_type}"
        
        def __eq__(self, other):
            return (self.buyer_num) == (other.buyer_num) 