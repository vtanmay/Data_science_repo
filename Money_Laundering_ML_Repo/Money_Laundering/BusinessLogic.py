import GFL.ejWebScraping as ejws
import GFL.ejPanda as ejpd
# wd=ejweb.ejWebOperations(ejShowBrowser=False,ejChromeDriverExePath="F:\ML\DataScienceProject\RiskPrediction\DRIVER\chromedriver.exe")
# result=wd.getPageSource(ejURL="www.rediffmail.com")
#print(result)

def getSearchURL(ejPageContent=None,ejXPath=None):
    allURLS=[]
    allWebElements = ejws.findMatchingElementsByXPath(ejPageContent=ejPageContent, ejXPath=ejXPath)
    for singlewe in allWebElements:
        url = ejws.getAttributeValue(ejWebElement=singlewe,ejAttributeName="href")
        allURLS.append(url)
    return allURLS
def getSearchText(ejPageContent=None,ejXPath=None):
    allText = []
    allWebElements = ejws.findMatchingElementsByXPath(ejPageContent=ejPageContent, ejXPath=ejXPath)
    for singlewe in allWebElements:
        txt = ejws.getInnerHTML(ejWebElement=singlewe)
        allText.append(txt)
    return allText
def getSearchTitle(ejPageContent=None,ejXPath=None):
    allTitle = []
    allWebElements = ejws.findMatchingElementsByXPath(ejPageContent=ejPageContent, ejXPath=ejXPath)
    for singlewe in allWebElements:
        txt = ejws.getText(ejWebElement=singlewe)
        allTitle.append(txt)
    return allTitle

def getMediaSitesDataFromExcelSheet(ejFilePath=None,ejSheetName=None):
    df = ejpd.readXLSFile(ejFilePath, ejSheetName)
    listData = ejpd.getColumnDataAsAListFromTable(ejDataFrame=df, ejOptColumnIndex=0)
    return listData
    # listData = []
    # nestedList = ejpd.readXLSFile(ejFilePath,ejSheetName).values.tolist()
    # # flatten nested list into a single list
    # for x in nestedList:
    #     for y in x:
    #         listData.append(y)
    # return listData

def getRegulatorySitesDataFromExcelSheet(ejFilePath=None, ejSheetName=None):
        df = ejpd.readXLSFile(ejFilePath, ejSheetName)
        listData = ejpd.getColumnDataAsAListFromTable(ejDataFrame=df,ejOptColumnIndex=1)
        return listData

def getRegulatorySitesDataFromExcelSheet(ejFilePath=None, ejSheetName=None):
        df = ejpd.readXLSFile(ejFilePath, ejSheetName)
        listData = ejpd.getColumnDataAsAListFromTable(ejDataFrame=df, ejOptColumnIndex=1)
        return listData

        # import os
#
#
#
# import ejagruti.GFL.ejPanda as ejpd
# import ejagruti.GFL.ejConfig as ejcfg
# import requests
# import ejagruti.GFL.ejWebScraper as ejws
# from bs4 import BeautifulSoup
# import re
# import mechanize
#
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#
#
# chrome_driver = "F:\ML\DataScienceProject\RiskPrediction\SERVER\chromedriver.exe"
# # go to Google and click the I'm Feeling Lucky button
#
# driver.get("https://www.google.co.in/search?q=narayan+murthy&start=00&sa=N")
# #print(driver.page_source)
# #driver.get("https://www.google.co.in/search?q=Riskpro+Reivew&start=01&sa=N")
# ejSearchResultURLXPath="//div[@class='rc']/div[@class='r']/a"
# ejSearchContentXPath="//div[@class='rc']/div[@class='s']//span[@class='st']"
# ejHeadersXPath="//div[@class='rc']/div[@class='r']//h3"
# allWE=driver.find_elements_by_xpath(ejSearchResultURLXPath)
# for e in allWE:
#     print(e.get_attribute("href")+"\n")
# allWE=driver.find_elements_by_xpath(ejSearchContentXPath)
# for e in allWE:
#     print(e.text+"\n")
# allWE=driver.find_elements_by_xpath(ejHeadersXPath)
# for e in allWE:
#     print(e.text+"\n")
# driver.quit()
#
#
# # test_host="127.0.0.1"
# # test_port=4545
# # server_url = "http://%s:%s/wd/hub" % (test_host, test_port)
# # dc = DesiredCapabilities.HTMLUNITWITHJS
# #
# # wd = webdriver.Remote(server_url, desired_capabilities={'browserName': 'htmlunit',
# #                          'version': '2',
# #                         'javascriptEnabled': False})
# # op=wd.get('https://www.google.co.in/search?q=apple+phone+review&start=40&sa=N')
# # print(op)
#
#
#
# #
# # def getSearchResultFromGoogle(ejSearchURL=None, ejSearchText=None, ejSearchResultUpToPage=0,ejRequestHeader=None,
# #                               ejSearchResultURLXPath="//div[@class='rc']/div[@class='r']/a",
# #                               ejSearchContentXPath="//div[@class='rc']/div[@class='s']//span[@class='st']",
# #                               ejHeadersXPath="//div[@class='rc']/div[@class='r']//h3"):
# #    url = ejSearchURL.replace("XXX", ejSearchText.replace(" ", "+")).replace("YYY", str(0))
# #    br = mechanize.Browser()
# #    br.set_handle_robots(False)
# #    br.addheaders = [('User-agent','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
# #    resp = br.open(url)
# #    print(resp.info())  # headers
# #    print(resp.read() ) # content
# #    print("")
# # def getAllMandatoryKeywords(ejFilePath=None):
# #    df= ejpd.readXLSFile(ejFilePath=ejFilePath,ejEitherSheetName="Mandatory Keywords")
# #    val=ejpd.getColumnDataAsAListFromTable(ejDataFrame=df,ejOptColumnIndex=0)
# #    return val
# #
# #
# # def getSearchResultFromGoogle1(ejSearchURL=None, ejSearchText=None, ejSearchResultUpToPage=0,ejRequestHeader=None,
# #                               ejSearchResultURLXPath="//div[@class='rc']/div[@class='r']/a",
# #                               ejSearchContentXPath="//div[@class='rc']/div[@class='s']//span[@class='st']",
# #                               ejHeadersXPath="//div[@class='rc']/div[@class='r']//h3"):
# #    # url="https://www.google.co.in/search?q=apple+phone+review&start=40&sa=N"
# #    hdrobj= ejws.getHeaderObject(ejListOfKeyValuePairs=ejRequestHeader.split("#,#"))
# #    for page_no in range(0, ejSearchResultUpToPage):
# #       url = ejSearchURL.replace("XXX", ejSearchText.replace(" ", "+")).replace("YYY", str(page_no))
# #
# #       r = requests.get(url,headers=hdrobj)
# #       soup = BeautifulSoup(r.content, 'html.parser')
# #       print(soup.prettify())
# #       matchingElements=soup.find_all("a")
# #       print(matchingElements)
# #
# #
