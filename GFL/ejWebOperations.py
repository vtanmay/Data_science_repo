from selenium.webdriver.chrome.options import Options
from selenium import webdriver
class ejWebOperations:
    driver=None
    # download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the
    # c:\DRIVER folder and makesure the name of the exe is chromedriver.exe and should be compatible with the current driver version
    def __init__(self, ejShowBrowser=False,ejChromeDriverExePath="D:\Data Science\Manish_Sir_class\MoneyLaundering_ML_Proj\Drivers\chromedriver.exe"):
        # instantiate a chrome options object so you can set the size and headless preference
        chrome_options = Options()
        if ejShowBrowser==False:
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--window-size=1920x1080")
            self.driver = webdriver.Chrome(options=chrome_options, executable_path=ejChromeDriverExePath)
        else:
            self.driver=webdriver.Chrome(executable_path=ejChromeDriverExePath)
    def launchURL(self,ejURL=None):
        self.driver.get(ejURL)
    def getPageSource(self,ejURL=None):
       if ejURL.upper().startswith("http"):
            self.driver.get(ejURL)
       else:
            self.driver.get("http://"+ejURL)
       return self.driver.page_source
    def getWebElements(self,ejXPath=None):
        return self.driver.find_elements_by_xpath(ejXPath)

    def getWebElement(self,ejXPath=None):
        return self.driver.find_element_by_xpath(ejXPath)
    def getAttributeValuesForTheGivenXPath(self,ejXPath=None,ejAttributeName=None):
        return self.driver.find_element_by_xpath(ejXPath).get_attribute(ejAttributeName)
    def getTextValuesForTheGivenXPath(self,ejXPath=None):
        return self.driver.find_element_by_xpath(ejXPath).text

            # def getHeaderObject(ejListOfKeyValuePairs=None):
        #     headers={}
        #     for kv in ejListOfKeyValuePairs:
        #         headers[kv.split(":")[0]]=kv.split(":")[1].strip()
        #     return headers
        # def getPageContent(ejURL=None,ejHeaderDictObj=None):
        #     if ejHeaderDictObj is None:
        #         page = requests.get(ejURL,headers={"User-Agent":"XY"})
        #     else:
        #         page=requests.get(ejURL,ejHeaderDictObj)
        #     page_html_code = BeautifulSoup(page.content, 'html.parser')
        #     return page.content
        # def getMatchingElementOrElementsByXPath(ejPageContent=None,ejXPath=None):
        #     dom=etree.HTML(ejPageContent)
        #     all_web_elements=dom.xpath(ejXPath)
        #     return all_web_elements
        # def getMatchingElementOrElementsByCSSSelector(ejPageContent=None,ejCSSSelector=None):
        #     soup = BeautifulSoup(ejPageContent, 'html.parser')
        #     obj=soup.select("div rc")
        #     return obj
        # def getChildElementsByXPath(ejWebElement=None,ejXPath=None):
        #     val=getInnerHTML(ejWebElement=ejWebElement)
        #     list= etree.HTML(val).xpath(ejXPath)
        #     return list
        # def getChildElementsByTagName(ejWebElement=None,ejTagName=None):
        #     list=[]
        #     for e in ejWebElement.iterchildren():
        #         if e.tag.upper()==ejTagName.upper():
        #             list.append(e)
        #     return list
        # def getTagNameOfTheElement(ejWebElement=None):
        #     return ejWebElement.tag
        # def getInnerHTML(ejWebElement=None):
        #     val=""
        #     for e in ejWebElement.iterchildren():
        #         val=val+str(etree.tostring(e))
        #     return val
        # def getAttribute(ejWebElement=None):
        #     return ejWebElement.attrib
        # def getText(ejWebElement=None):
        #     return ejWebElement.text
        # def getValueByCSSSelector(ejPageContent=None,ejCSS=None):
        #     soupobj = BeautifulSoup(ejPageContent, 'html.parser')
        #     val=eval("soupobj."+ejCSS)
        #     return val
        #
        # #
        # # op=fop.readEntireFile(ejFilePath="f:\html.txt")
        # # pobj=findMatchingElementOrElementsByXPath(ejPageContent=op,ejXPath="//td[.='FII']/..")
        # # getChildElement(ejWebElement=pobj[0],ejTagName="td")
        # # print(pobj.tag)
        # #op=getPageContent(ejURL="https://fnoanalysis.com/oi/fo_part_idx_dtls.php")
        # #op = getPageContent(ejURL="http://server:90/finsys")
