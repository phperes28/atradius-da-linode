

da_type = (
    ("1 - NNP Info", "1 - NNP Info"),
    ("2 - NNP WD", "2 - NNP WD"),
    ("3 - Claims WD", "3 - Claims WD"),
    ("4 - SR Request", "4 - SR Request"),
    ("5 - DA First Contact", "5 -  DA First Contact"),
    ("6 - DA Annual Review ", "6 -  DA Annual Review"),
    ("7 - DA Annual Review no Supplier", "7 - DA Annual Review no Supplier"),
    ("8 DA - Follow Up", "8 - DA Follow Up"),
    ( "9 - DA Follow Up 2", "9 - DA Follow Up 2"),
    ("10- DA Follow Up 3","10 - DA Follow Up 3")
    )



def generate_first_contact(buyer_number, buyer_name, contact_name,  supplier, fins_1, fins_2, sender ):
    #IF fins_2 == Nul - use another script
    return (f"""Atradius Information Request -  {buyer_name}// Atradius Ref. {buyer_number} \n

Hi {contact_name}, 

I hope you are doing well. 

We are conducting a review on {buyer_name} in consideration of an application for trade credit insurance cover received from your supplier {supplier}.\n
In order for us to assist your supplier with insurance cover, we would appreciate it if you could please provide the following: \n
- {fins_1}\n
- {fins_2}\n
If the audited numbers are unavailable, we would appreciate any draft or interim management accounts.\n
All information supplied to us is treated on a confidential basis and is for internal assessment purposes only and is not passed onto a third party without your prior consent.\n
I am happy to provide a confidentiality agreement, please advise if this is required.\n
About Atradius:\n
Atradius, one of the world's leading credit insurance and credit management companies, protects more than EUR400 billion of the world trade annually against the risks of non-payment.
Head-quartered in Amsterdam, the group has a presence in more than 50 countries on five continents, employing around 3,700 people with and annual turnover of EUR1.8 billion,\n giving us a 24% per cent global market share. 
Our company which has a wealth of knowledge on trade sectors, countries and business trends, makes more than 20,000 credit decisions daily.\n

Should you have any queries or wish to further discuss the details, please do not hesitate to contact me.\n

Thank you, \n

{sender}""")


def generate_annual_review_with_supplier(buyer_number, buyer_name, contact_name, fins_1, fins_2, previous_contact, sender):

    return(f"""Atradius Information Request -  {buyer_name}// Atradius Ref. {buyer_number}
    \n\nHi {contact_name}, 
    
    I hope this email find you well.\n
    
    You spoke to my colleague, {previous_contact} previously and you kindly sent through confidential financials for {buyer_name} (refer to correspondence below).\n
    Would you please assist us once again as we are conducting an annual review on {buyer_name} and we require updated financial information so we are able to make a proper risk assessment.\n
    Based on this information we will decide whether to roll over your status as covered buyer in our database.\n 
    Can you kindly provide the following:\n
    - {fins_1}\n
    - {fins_2}
    
    If the audited numbers are unavailable, we would appreciate any draft or interim management accounts.
    
    All information supplied to us is treated on a confidential basis and is for internal assessment purposes only and is not passed onto a third party without your prior consent.
     I am happy to provide a confidentiality agreement, please advise if this is required.
    
    About Atradius:
    Atradius, one of the world's leading credit insurance and credit management companies, protects more than EUR400 billion of the world trade annually against the risks of non-payment.
    Head-quartered in Amsterdam, the group has a presence in more than 50 countries on five continents, employing around 3,700 people with and annual turnover of EUR1.8 billion, giving 
    us a 24% per cent global market share. Our company which has a wealth of knowledge on trade sectors, countries and business trends, makes more than 20,000 credit decisions daily.\n
    
    Should you have any queries or wish to further discuss the details, please do not hesitate to contact me.
    
    Thank you, 
    
    {sender}""")

def generate_annual_review_no_supplier(buyer_number, buyer_name, contact_name, fins_1, fins_2, previous_contact):
#make tkinter display following text

    return(f"""Atradius Information Request -  {buyer_name}// Atradius Ref. {buyer_number}\n

    Hello {contact_name}\n
    
    Hope you are well.\n
    
    I would like to refer to previous contact with our company. Previously, you have provided my colleague {previous_contact} with annual accounts of {buyer_name}. \n
    The company is due for another review hence I wanted to check if we could get hold of {fins_1} and {fins_2}?\n
     
    All information supplied to us is treated on a confidential basis and is for internal assessment purposes only and is not passed onto a third party. If you have any queries, or would like to discuss further, please don’t hesitate to contact me.\n
     
    Thank you!!\n
    
    Kind Regards,""")


def generate_NNP_info(buyer_number, buyer_name, contact_name, supplier):

    return(f"""NNP -{buyer_name}// Atradius Ref. {buyer_number}\n
    
    Hello {contact_name}
    
    Hope you are well.\n

    Can you please provide more information on NPP reported by {supplier} on {buyer_name} {buyer_number}?\n

    Thank you""")


# def generate_NNP_WD(buyer_number, buyer_name, contact_name, supplier):

#     return(f"""NNP -{buyer_name}// Atradius Ref. {buyer_number}\n
    
#     Hello {contact_name}
    
#     Hope you are well.\n

#     Can you please provide more information on NPP reported by {supplier} on {buyer_name} {buyer_number}?\n

#     Thank you""")




def generate_claims_WD(buyer_number, buyer_name, contact_name, supplier):
    return(f"""NNP -{buyer_name}// Atradius Ref. {buyer_number}\n
    
    Hello {contact_name}
    
    Hope you are well.\n

    NPP reported by {supplier} on {buyer_name} {buyer_number} is now with claims/collections\n
    Can you please let the customer know we are withdrawing their limit effective immediately?

    Thank you""")