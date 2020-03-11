import GFL.ejFileOperations as ejfo
import GFL.ejWebScraping as ejws
import Money_Laundering_ML_Repo.Money_Laundering.BusinessLogic as bl
import GFL.ejListOperations as ejLst

titleList=[]
urlList = []
textList = []

# scrap data from google search pages.
ejSearchContent= "dsk developers ltd"
ejPageNumber=8
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

# read media sites data from excel
loc = (ejfo.getCurrentWorkingDirecotry()+"\RiskPrediction2017.xlsx")
listOfMediaSites = bl.getMediaSitesDataFromExcelSheet(loc,"Media Sites")

# read regulatory sites data from excel
listOfRegulatorySites = bl.getRegulatorySitesDataFromExcelSheet(loc,"Regulatory Websites")

# perform data clean up on regulatory sites data from excel
urlList1 = ejLst.getListAfterRemovingParticularCharSeq(ejList=listOfRegulatorySites, ejCharSeq='http://www.')
urlList2 = ejLst.getListAfterRemovingParticularCharSeq(ejList=urlList1, ejCharSeq='https://www.')
urlList3 = ejLst.getListAfterRemovingParticularCharSeq(ejList=urlList2, ejCharSeq='https://')
urlList4 = ejLst.getListAfterRemovingParticularCharSeq(ejList=urlList3, ejCharSeq='www.')
urlList5 = ejLst.getListAfterRemovingParticularCharSeq(ejList=urlList4, ejCharSeq='http://')
urlList6 = ejLst.getListAfterRemovingParticularCharSeq(ejList=urlList5, ejCharSeq='\xa0')

# perform split operation to retrieve only domain name.
finalRegUrlListAfterCleanup = ejLst.getListAfterSpliting(ejList=urlList6, ejSeparator='/', ejMaxSplit=1, ejSplitPart=0)

# perform search in media site and regulatory list.
urlsMatchedWithMediaSites = bl.getUrlsWithMediaOrRegulatoryWebsites(ejAllUrlList=urlList, ejMediaOrRegulatoryList=listOfMediaSites)
urlsMatchedWithRegulatorySites = bl.getUrlsWithMediaOrRegulatoryWebsites(ejAllUrlList=urlList, ejMediaOrRegulatoryList=finalRegUrlListAfterCleanup)

print("==== matched urls with media sites===", urlsMatchedWithMediaSites)
print("==== matched urls with regulatory sites===", urlsMatchedWithRegulatorySites)
print("==== final list====", [*urlsMatchedWithMediaSites, *urlsMatchedWithRegulatorySites])
print("==== final list count of links ====", len([*urlsMatchedWithMediaSites, *urlsMatchedWithRegulatorySites]))