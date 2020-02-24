import requests
from bs4 import BeautifulSoup
import GFL.ejFileOperations as fop
from lxml import etree

def getHeaderObject(ejListOfKeyValuePairs=None):
    headers={}
    for kv in ejListOfKeyValuePairs:
        headers[kv.split(":")[0]]=kv.split(":")[1]
    return headers
def getPageContent(ejURL=None,ejHeaderDictObj=None):
    if ejHeaderDictObj is None:
        page = requests.get(ejURL,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"})
    else:
        page=requests.get(ejURL,headers=ejHeaderDictObj)
    page_html_code = BeautifulSoup(page.content, 'html.parser')
    return page.content
def findMatchingElementsByXPath(ejPageContent=None,ejXPath=None):
    dom=etree.HTML(ejPageContent)
    all_web_elements=dom.xpath(ejXPath)
    return all_web_elements

def getChildElementsByXPath(ejWebElement=None,ejXPath=None):
    val=getInnerHTML(ejWebElement=ejWebElement)
    list= etree.HTML(val).xpath(ejXPath)
    return list
def getChildElementsByTagName(ejWebElement=None,ejTagName=None):
    list=[]
    for e in ejWebElement.iterchildren():
        if e.tag.upper()==ejTagName.upper():
            list.append(e)
    return list
def getTagNameOfTheElement(ejWebElement=None):
    return ejWebElement.tag
def getInnerHTML(ejWebElement=None):
    val=""
    for e in ejWebElement.iterchildren():
        val=val+str(etree.tostring(e))
    return val
def getAttributeName(ejWebElement=None):
    return ejWebElement.attrib
def getAttributeValue(ejWebElement=None,ejAttributeName=None):
    return ejWebElement.attrib[ejAttributeName]
def getText(ejWebElement=None):
    return ejWebElement.text

def getValueByCSSSelector(ejPageContent=None,ejCSS=None):
    soupobj = BeautifulSoup(ejPageContent, 'html.parser')
    val=eval("soupobj."+ejCSS)
    return val

#
# op=fop.readEntireFile(ejFilePath="f:\html.txt")
# pobj=findMatchingElementOrElementsByXPath(ejPageContent=op,ejXPath="//td[.='FII']/..")
# getChildElement(ejWebElement=pobj[0],ejTagName="td")
# print(pobj.tag)
#op=getPageContent(ejURL="https://fnoanalysis.com/oi/fo_part_idx_dtls.php")
#op = getPageContent(ejURL="http://server:90/finsys")
