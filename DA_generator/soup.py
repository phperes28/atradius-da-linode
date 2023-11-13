import requests 
from bs4 import BeautifulSoup
from urllib import request,response

cookies = {
    '_ga': 'GA1.3.269297806.1697444380',
    'SearchCountry': 'AUS',
    'SearchMethod': 'Commercial Search',
    'dtCookie': 'v_4_srv_6_sn_F16C1547C7D023816CD4DA13567C3E12_perc_100000_ol_0_mul_1_app-3A781331891d8dfcc0_1',
    'rxVisitor': '1697495942779A3ETU5QVDOPF4V3O4L7N61D5FDFCVTHG',
    'InitialFilterUrl': 'eyJGaWx0ZXJlZCI6ZmFsc2UsIkZpbHRlckNvbGxhcHNlZCI6dHJ1ZSwiSW5pdGlhbEZpbHRlckRlc2NyaXB0aW9uIjpudWxsLCJJbml0aWFsRmlsdGVyVXJsIjpudWxsLCJGaWx0ZXJUeXBlIjpudWxsLCJEb3dubG9hZCI6ZmFsc2UsIkRvd25sb2FkRmlsdGVyZWQiOmZhbHNlLCJQYWdlTnVtYmVyIjpudWxsLCJJbnZlc3RpZ2F0aW9uUGFnZU51bWJlciI6bnVsbCwiRm9jdXNUYWIiOm51bGwsIlNvcnRCeSI6bnVsbCwiU29ydERpcmVjdGlvbiI6bnVsbCwiTmFtZSI6bnVsbCwiSWRUeXBlIjpudWxsLCJJZFZhbHVlIjpudWxsLCJEYXRlRnJvbSI6bnVsbCwiRGF0ZVRvIjpudWxsLCJMYXN0UmV2aWV3ZWRCeSI6bnVsbCwiTGFzdExQUlR5cGUiOm51bGwsIkxhc3RMUFJGaWx0ZXIiOm51bGwsIk92ZXJkdWVDcml0ZXJpYSI6bnVsbCwiT3ZlcmR1ZSI6bnVsbCwiT3ZlcmR1ZVRvIjpudWxsLCJPdmVyZHVlRnJvbSI6bnVsbCwiT3V0c3RhbmRpbmdDcml0ZXJpYSI6bnVsbCwiT3V0c3RhbmRpbmciOm51bGwsIk91dHN0YW5kaW5nVG8iOm51bGwsIk91dHN0YW5kaW5nRnJvbSI6bnVsbCwiTGFzdEV4cG9zdXJlQ3JpdGVyaWEiOm51bGwsIkxhc3RFeHBvc3VyZSI6bnVsbCwiTGFzdEV4cG9zdXJlRnJvbSI6bnVsbCwiTGFzdEV4cG9zdXJlVG8iOm51bGwsIlBpRmlsdGVyIjpudWxsLCJHcm91cHMiOltdLCJNb25pdG9yaW5nUHJvZmlsZXMiOltdLCJDb3VudHJ5IjpbXSwiU3RhdGUiOltdLCJGYWlsdXJlUmlzayI6W10sIkxhdGVQYXltZW50UmlzayI6W10sIkZhaWx1cmVSaXNrVHJlbmQiOltdLCJMYXRlUGF5bWVudFJpc2tUcmVuZCI6W10sIlJlcG9ydFR5cGUiOltdLCJMZWRnZXIiOltdLCJBbGVydFR5cGVHZW5lcmFsIjpbXSwiTWVzc2FnZVR5cGUiOltdLCJSZWFkIjpbXSwiQWxlcnRUeXBlRnIiOltdLCJBbGVydFR5cGVMcHIiOltdLCJDb21wYW55VHlwZSI6W10sIkNvbXBhbnlTdGF0dXMiOltdLCJJbnZlc3RpZ2F0aW9uIjpbXSwiQ3VycmVudExQUiI6W119',
    'EntityFilterModel': 'eyJGaWx0ZXJlZCI6ZmFsc2UsIkZpbHRlckNvbGxhcHNlZCI6dHJ1ZSwiSW5pdGlhbEZpbHRlckRlc2NyaXB0aW9uIjpudWxsLCJJbml0aWFsRmlsdGVyVXJsIjpudWxsLCJGaWx0ZXJUeXBlIjpudWxsLCJEb3dubG9hZCI6ZmFsc2UsIkRvd25sb2FkRmlsdGVyZWQiOmZhbHNlLCJQYWdlTnVtYmVyIjpudWxsLCJJbnZlc3RpZ2F0aW9uUGFnZU51bWJlciI6bnVsbCwiRm9jdXNUYWIiOm51bGwsIlNvcnRCeSI6bnVsbCwiU29ydERpcmVjdGlvbiI6bnVsbCwiTmFtZSI6bnVsbCwiSWRUeXBlIjpudWxsLCJJZFZhbHVlIjpudWxsLCJEYXRlRnJvbSI6bnVsbCwiRGF0ZVRvIjpudWxsLCJMYXN0UmV2aWV3ZWRCeSI6bnVsbCwiTGFzdExQUlR5cGUiOm51bGwsIkxhc3RMUFJGaWx0ZXIiOm51bGwsIk92ZXJkdWVDcml0ZXJpYSI6bnVsbCwiT3ZlcmR1ZSI6bnVsbCwiT3ZlcmR1ZVRvIjpudWxsLCJPdmVyZHVlRnJvbSI6bnVsbCwiT3V0c3RhbmRpbmdDcml0ZXJpYSI6bnVsbCwiT3V0c3RhbmRpbmciOm51bGwsIk91dHN0YW5kaW5nVG8iOm51bGwsIk91dHN0YW5kaW5nRnJvbSI6bnVsbCwiTGFzdEV4cG9zdXJlQ3JpdGVyaWEiOm51bGwsIkxhc3RFeHBvc3VyZSI6bnVsbCwiTGFzdEV4cG9zdXJlRnJvbSI6bnVsbCwiTGFzdEV4cG9zdXJlVG8iOm51bGwsIlBpRmlsdGVyIjpudWxsLCJHcm91cHMiOltdLCJNb25pdG9yaW5nUHJvZmlsZXMiOltdLCJDb3VudHJ5IjpbIkFVUyJdLCJTdGF0ZSI6W10sIkZhaWx1cmVSaXNrIjpbXSwiTGF0ZVBheW1lbnRSaXNrIjpbXSwiRmFpbHVyZVJpc2tUcmVuZCI6W10sIkxhdGVQYXltZW50Umlza1RyZW5kIjpbXSwiUmVwb3J0VHlwZSI6W10sIkxlZGdlciI6W10sIkFsZXJ0VHlwZUdlbmVyYWwiOltdLCJNZXNzYWdlVHlwZSI6W10sIlJlYWQiOltdLCJBbGVydFR5cGVGciI6W10sIkFsZXJ0VHlwZUxwciI6W10sIkNvbXBhbnlUeXBlIjpbXSwiQ29tcGFueVN0YXR1cyI6W10sIkludmVzdGlnYXRpb24iOltdLCJDdXJyZW50TFBSIjpbXX0=',
    '__RequestVerificationToken_L2ludGVnYXRl0': 'RnUKV_bSIVWXIG0GMWA1vGqCCibV3E3TRDOUrnTOU4kUlhv4A3z9LDeKX7ndm3LRArGSxzhobUGJk4zC50yoiY5C7BhAP581aFWGcA-e9vw1',
    'NSC_80-jmmjpoejsfdu.dpn.bv': 'ffffffffc3a0713245525d5f4f58455e445a4a423660',
    '_gid': 'GA1.3.1662799597.1698044320',
    'id': 'xry4ej00uu5hilk22wl2fcno',
    '_tempID': '',
    '_gat': '1',
    '_gat_UA-215544878-1': '1',
    'rxvt': '1698046220484|1698044319505',
    'dtPC': '6$44420332_916h-vDAUBFRRCABKEKBUMTAKPRIRPGVURTEJR-0e0',
    '_ga_EVJJECRXVC': 'GS1.3.1698044320.8.1.1698044420.60.0.0',
    '_ga_T6X5KWDHKY': 'GS1.3.1698044320.8.1.1698044420.60.0.0',
    'dtSa': 'true%7CC%7C-1%7CSign%20in%7C-%7C1698044427279%7C44420332_916%7Chttps%3A%2F%2Filliondirect.com.au%2Fintegate%2FLogin.mvc%7C%7C%7C%7C',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en,pt-BR;q=0.9,pt;q=0.8,en-US;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': '_ga=GA1.3.269297806.1697444380; SearchCountry=AUS; SearchMethod=Commercial Search; dtCookie=v_4_srv_6_sn_F16C1547C7D023816CD4DA13567C3E12_perc_100000_ol_0_mul_1_app-3A781331891d8dfcc0_1; rxVisitor=1697495942779A3ETU5QVDOPF4V3O4L7N61D5FDFCVTHG; InitialFilterUrl=eyJGaWx0ZXJlZCI6ZmFsc2UsIkZpbHRlckNvbGxhcHNlZCI6dHJ1ZSwiSW5pdGlhbEZpbHRlckRlc2NyaXB0aW9uIjpudWxsLCJJbml0aWFsRmlsdGVyVXJsIjpudWxsLCJGaWx0ZXJUeXBlIjpudWxsLCJEb3dubG9hZCI6ZmFsc2UsIkRvd25sb2FkRmlsdGVyZWQiOmZhbHNlLCJQYWdlTnVtYmVyIjpudWxsLCJJbnZlc3RpZ2F0aW9uUGFnZU51bWJlciI6bnVsbCwiRm9jdXNUYWIiOm51bGwsIlNvcnRCeSI6bnVsbCwiU29ydERpcmVjdGlvbiI6bnVsbCwiTmFtZSI6bnVsbCwiSWRUeXBlIjpudWxsLCJJZFZhbHVlIjpudWxsLCJEYXRlRnJvbSI6bnVsbCwiRGF0ZVRvIjpudWxsLCJMYXN0UmV2aWV3ZWRCeSI6bnVsbCwiTGFzdExQUlR5cGUiOm51bGwsIkxhc3RMUFJGaWx0ZXIiOm51bGwsIk92ZXJkdWVDcml0ZXJpYSI6bnVsbCwiT3ZlcmR1ZSI6bnVsbCwiT3ZlcmR1ZVRvIjpudWxsLCJPdmVyZHVlRnJvbSI6bnVsbCwiT3V0c3RhbmRpbmdDcml0ZXJpYSI6bnVsbCwiT3V0c3RhbmRpbmciOm51bGwsIk91dHN0YW5kaW5nVG8iOm51bGwsIk91dHN0YW5kaW5nRnJvbSI6bnVsbCwiTGFzdEV4cG9zdXJlQ3JpdGVyaWEiOm51bGwsIkxhc3RFeHBvc3VyZSI6bnVsbCwiTGFzdEV4cG9zdXJlRnJvbSI6bnVsbCwiTGFzdEV4cG9zdXJlVG8iOm51bGwsIlBpRmlsdGVyIjpudWxsLCJHcm91cHMiOltdLCJNb25pdG9yaW5nUHJvZmlsZXMiOltdLCJDb3VudHJ5IjpbXSwiU3RhdGUiOltdLCJGYWlsdXJlUmlzayI6W10sIkxhdGVQYXltZW50UmlzayI6W10sIkZhaWx1cmVSaXNrVHJlbmQiOltdLCJMYXRlUGF5bWVudFJpc2tUcmVuZCI6W10sIlJlcG9ydFR5cGUiOltdLCJMZWRnZXIiOltdLCJBbGVydFR5cGVHZW5lcmFsIjpbXSwiTWVzc2FnZVR5cGUiOltdLCJSZWFkIjpbXSwiQWxlcnRUeXBlRnIiOltdLCJBbGVydFR5cGVMcHIiOltdLCJDb21wYW55VHlwZSI6W10sIkNvbXBhbnlTdGF0dXMiOltdLCJJbnZlc3RpZ2F0aW9uIjpbXSwiQ3VycmVudExQUiI6W119; EntityFilterModel=eyJGaWx0ZXJlZCI6ZmFsc2UsIkZpbHRlckNvbGxhcHNlZCI6dHJ1ZSwiSW5pdGlhbEZpbHRlckRlc2NyaXB0aW9uIjpudWxsLCJJbml0aWFsRmlsdGVyVXJsIjpudWxsLCJGaWx0ZXJUeXBlIjpudWxsLCJEb3dubG9hZCI6ZmFsc2UsIkRvd25sb2FkRmlsdGVyZWQiOmZhbHNlLCJQYWdlTnVtYmVyIjpudWxsLCJJbnZlc3RpZ2F0aW9uUGFnZU51bWJlciI6bnVsbCwiRm9jdXNUYWIiOm51bGwsIlNvcnRCeSI6bnVsbCwiU29ydERpcmVjdGlvbiI6bnVsbCwiTmFtZSI6bnVsbCwiSWRUeXBlIjpudWxsLCJJZFZhbHVlIjpudWxsLCJEYXRlRnJvbSI6bnVsbCwiRGF0ZVRvIjpudWxsLCJMYXN0UmV2aWV3ZWRCeSI6bnVsbCwiTGFzdExQUlR5cGUiOm51bGwsIkxhc3RMUFJGaWx0ZXIiOm51bGwsIk92ZXJkdWVDcml0ZXJpYSI6bnVsbCwiT3ZlcmR1ZSI6bnVsbCwiT3ZlcmR1ZVRvIjpudWxsLCJPdmVyZHVlRnJvbSI6bnVsbCwiT3V0c3RhbmRpbmdDcml0ZXJpYSI6bnVsbCwiT3V0c3RhbmRpbmciOm51bGwsIk91dHN0YW5kaW5nVG8iOm51bGwsIk91dHN0YW5kaW5nRnJvbSI6bnVsbCwiTGFzdEV4cG9zdXJlQ3JpdGVyaWEiOm51bGwsIkxhc3RFeHBvc3VyZSI6bnVsbCwiTGFzdEV4cG9zdXJlRnJvbSI6bnVsbCwiTGFzdEV4cG9zdXJlVG8iOm51bGwsIlBpRmlsdGVyIjpudWxsLCJHcm91cHMiOltdLCJNb25pdG9yaW5nUHJvZmlsZXMiOltdLCJDb3VudHJ5IjpbIkFVUyJdLCJTdGF0ZSI6W10sIkZhaWx1cmVSaXNrIjpbXSwiTGF0ZVBheW1lbnRSaXNrIjpbXSwiRmFpbHVyZVJpc2tUcmVuZCI6W10sIkxhdGVQYXltZW50Umlza1RyZW5kIjpbXSwiUmVwb3J0VHlwZSI6W10sIkxlZGdlciI6W10sIkFsZXJ0VHlwZUdlbmVyYWwiOltdLCJNZXNzYWdlVHlwZSI6W10sIlJlYWQiOltdLCJBbGVydFR5cGVGciI6W10sIkFsZXJ0VHlwZUxwciI6W10sIkNvbXBhbnlUeXBlIjpbXSwiQ29tcGFueVN0YXR1cyI6W10sIkludmVzdGlnYXRpb24iOltdLCJDdXJyZW50TFBSIjpbXX0=; __RequestVerificationToken_L2ludGVnYXRl0=RnUKV_bSIVWXIG0GMWA1vGqCCibV3E3TRDOUrnTOU4kUlhv4A3z9LDeKX7ndm3LRArGSxzhobUGJk4zC50yoiY5C7BhAP581aFWGcA-e9vw1; NSC_80-jmmjpoejsfdu.dpn.bv=ffffffffc3a0713245525d5f4f58455e445a4a423660; _gid=GA1.3.1662799597.1698044320; id=xry4ej00uu5hilk22wl2fcno; _tempID=; _gat=1; _gat_UA-215544878-1=1; rxvt=1698046220484|1698044319505; dtPC=6$44420332_916h-vDAUBFRRCABKEKBUMTAKPRIRPGVURTEJR-0e0; _ga_EVJJECRXVC=GS1.3.1698044320.8.1.1698044420.60.0.0; _ga_T6X5KWDHKY=GS1.3.1698044320.8.1.1698044420.60.0.0; dtSa=true%7CC%7C-1%7CSign%20in%7C-%7C1698044427279%7C44420332_916%7Chttps%3A%2F%2Filliondirect.com.au%2Fintegate%2FLogin.mvc%7C%7C%7C%7C',
    'Origin': 'https://illiondirect.com.au',
    'Referer': 'https://illiondirect.com.au/integate/Login.mvc',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

# data = 'Email=pedro.peres%40atradius.com&Password=Aupper1289*'

data = {"Email" : "pedro.peres@atradius.com",
        "Password" : "Aupper1289*"}




with requests.Session() as s:
    login_url = "https://illiondirect.com.au/integate/"
    r = s.get(login_url)
    # soup = BeautifulSoup(r.text, "html.parser")

    p = s.post(login_url, data=data, headers=headers, cookies=r.cookies, allow_redirects=False)
   
    print(p.status_code)
    print(p.headers) 

    complete_login  ="/integate/Landing.mvc?upid=6383369120632530701071260884&referrer=Login"

 

    search_url = "https://illiondirect.com.au/integate/Search.mvc?upid=6383368481792633152143187946&search=004377780&initialCountry=AUS&method=Commercial%20Search"