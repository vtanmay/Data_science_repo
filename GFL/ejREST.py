import requests
import json
from lxml import html
from bs4 import BeautifulSoup
def requestGET(ej_url=None,ej_timeoutseconds=None):
    print(ej_url)
    response= requests.get(ej_url,timeout=ej_timeoutseconds,headers={"User-Agent":"XY"})
    return response.text
    #dictionary={"status_code":response.status_code,"text":response.text,"headers":response.headers,"url":response.url,"header_links":response.links}
    #return dictionary
def requestPOST(ejRequestURL=None,ejJSONPostData=None,ejHeaders=None):
    response = requests.request("POST", ejRequestURL, data=ejJSONPostData, headers=ejHeaders)
    return response.text


# import requests
#
# url = "https://www.niftyindices.com/Backpage.aspx/getHistoricaldatatabletoString"
#
# payload = "{'name': 'NIFTY 50', 'startDate': '01-Jan-2020', 'endDate': '21-Jan-2020'}"
# headers = {
# 'Accept': 'application/json, text/javascript, */*; q=0.01',
# 'X-Requested-With': 'XMLHttpRequest',
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
# 'Content-Type': 'application/json; charset=UTF-8',
#  }
#
# requests.post(url,data=payload,json=payload,headers=headers)
# response = requests.request("POST", url, data=payload, headers=headers)


#{'name': 'NIFTY 50', 'startDate': '01-Jan-2020', 'endDate': '21-Jan-2020'}
#requestGET(ej_url="http://portal.amfiindia.com/DownloadNAVHistoryReport_Po.aspx?mf=3&tp=1&frmdt=01-Jan-2008&todt=10-Dec-2008",ej_timeoutseconds=30)
 #https://nseindia.com/api/option-chain-indices?symbol=BANKNIFTY

#
# #response= requests.get("http://dummy.restapiexample.com/api/v1/employee/1",timeout=30, headers={"User-Agent":"XY"})
# #print(response.json())
# obj=RESTOperations()
# dict=obj.requestGET("https://nseindia.com/api/option-chain-indices?symbol=BANKNIFTY",20)
# print(str(dict.get("text")))
# print("aaa")