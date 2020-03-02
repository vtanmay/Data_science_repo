import os
import GFL.ejConfig as ejconf
import GFL.ejGeneric as ejgen
import GFL.ejFileOperations as ejfo
import GFL.ejWebScraping as ejws
import Money_Laundering_ML_Repo.Money_Laundering.BusinessLogic as bl
import re
from itertools import compress
import pandas as pd
import GFL.ejStats as ejsts
# cnfdict=ejconf.readConfigFile(ejConfigFilePath=os.getcwd()+"/config.ini")#read config file
# filepath=cnfdict["RISK"]["file_path"]#get file path
# listofmandatorykeywords=bl.getAllMandatoryKeywords(ejFilePath=filepath)
# google_url=cnfdict["GOOGLE"]["search_url"]
# prefix=cnfdict["GOOGLE"]["prefix"]
# dict=bl.getSearchResultFromGoogle(ejSearchURL=google_url,ejSearchText="riskpro pune review",ejSearchResultUpToPage=5)
titleList=[]
urlList = []
newUrlList = []
textList = []
newRegulatoryUrlList = []

ejSearchContent="Vijay mallya"
ejPageNumber=5
search_url="https://www.google.co.in"
prefix="/search?q=XXX&start=YYY0&sa=N"
ejSearchResultURLXPath="//div[@class='rc']/div[@class='r']/a"
ejSearchContentXPath="//div[@class='rc']/div[@class='s']//span[@class='st']"
ejHeadersXPath="//div[@class='rc']/div[@class='r']//h3"
for pn in range(0,ejPageNumber):
    htmlcode=ejws.getPageContent(ejURL=search_url+prefix.replace("XXX",ejSearchContent).replace("YYY",str(pn)))
    allURLSOnSinglePage=bl.getSearchURL(ejPageContent=htmlcode,ejXPath=ejSearchResultURLXPath)
    allTexts=bl.getSearchText(ejPageContent=htmlcode,ejXPath=ejSearchContentXPath)
    allTitle=bl.getSearchTitle(ejPageContent=htmlcode,ejXPath=ejHeadersXPath)
    urlList.extend(allURLSOnSinglePage)
    textList.extend(allTexts)
    titleList.extend(allTitle)

print("==== all URLs ====", urlList)
#print("==== all Text ====", textList)
#print("==== all Titles ====", titleList)

# read media sites data from excel
#D:\Personal\ML\Data_science_repo
#D:\Data Science\Manish_Sir_class\Data_science_repo\DataSheet\RiskPrediction2017.xlsx
loc = (ejfo.getCurrentWorkingDirecotry()+"\RiskPrediction2017.xlsx")
listOfMediaSites = bl.getMediaSitesDataFromExcelSheet(loc,"Media Sites")
print("==== list of media sites data from excel ======")
print(listOfMediaSites)

# read regulatory sites data from excel
listOfRegulatorySites = bl.getRegulatorySitesDataFromExcelSheet(loc,"Regulatory Websites")
print("==== list of regulatory sites data from excel =====")
print(listOfRegulatorySites)

# get all URLs after splitting
#urlListAfterSplit = bl.getAllUrlsAfterSpliting(ejList=urlList, ejSeparator='//',ejMaxSplit=1)[1]

for i in urlList:
    newUrlList.append(i.split('//', 1)[1].split('/', 1)[0])

print("===== split url list====", newUrlList)
tempList = []

for i in listOfMediaSites:
    if 'http' in i:
        tempList.append(i.split('//', 1)[1].split('/', 1)[0].split('.', 1)[0])
    tempList.append(i.split('.', 1)[0])

print("===== extract domain name for media sites from excel===", tempList)



#for i in listOfRegulatorySites:
#    newRegulatoryUrlList.append(i.split('//', 1)[1].split('/', 1)[0])

#print("===== split regulatory url list====", newRegulatoryUrlList)

#for i in range(len(listOfMediaSites)):
   # for j in newUrlList:
  #      if listOfMediaSites[i]  == 'hindustantimes.com':
  #          listWithFilter1.append(listOfMediaSites[i])
    #if i == 'hindustantimes.com':



# compare
# verify keywords.

#  #Add list to data frame
# df = pd.DataFrame({'Titles': titleList, 'Links': urlList, 'Text': textList})
# #dumping data into CSV.
# df.to_csv('dskDeveloperInfoUpdated.csv', index=False, encoding='utf-8')

