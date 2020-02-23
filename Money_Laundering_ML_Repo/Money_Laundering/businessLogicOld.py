import GFL.ejWebScraping as ejws


def getSearchResultTitle(ejURL=None, ejXPath=None):
    pageContent = ejws.getPageContent(ejURL=ejURL,ejHeaderDictObj={"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36"})
    allTitles = ejws.findMatchingElementOrElementsByXPath(ejPageContent=pageContent,ejXPath=ejXPath)
    return allTitles

def getSearchResultUrl(ejURL=None, ejXPath=None):
    pageContent = ejws.getPageContent(ejURL=ejURL,ejHeaderDictObj={"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36"})
    allUrls = ejws.findMatchingElementOrElementsByXPath(ejPageContent=pageContent,ejXPath=ejXPath)
    return allUrls

def getSearchResultText(ejURL=None, ejXPath=None):
    pageContent = ejws.getPageContent(ejURL=ejURL,ejHeaderDictObj={"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36"})
    allText = ejws.findMatchingElementOrElementsByXPath(ejPageContent=pageContent,ejXPath=ejXPath)
    return allText

# def getSearchResultText(ejURL=None, ejQSS=None):
#     pageContent = ejws.getPageContent(ejURL=ejURL,ejHeaderDictObj={"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36"})
#     allText = ejws.getValueByQuerySelector(ejPageContent=pageContent,ejQSS=ejQSS)
#     return allText

