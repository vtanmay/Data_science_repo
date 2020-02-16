import GFL.ejWebScraping as ejbs

# get page content
var = ejbs.getPageContent(ejURL="https://www.google.com/search?q=dsk+developers+ltd&oq=dsk+developers+ltd&aqs=chrome..69i57.10393j0j7&sourceid=chrome&ie=UTF-8")
# https://www.google.com/search?q=DSK+developers&oq=DSK+developers&aqs=chrome..69i57.18838j0j7&sourceid=chrome&ie=UTF-8
print("=====page html code====== ",var)

#//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]

allLinks = ejbs.findMatchingElementOrElementsByXPath(ejPageContent=var, ejXPath='//a')
print("==== all links ====",  allLinks)
print("==== count of all links ====",  len(allLinks))



# get attribute link value
attr = ejbs.getAttribute(ejWebElement=allLinks[20])
print("====== attributes ===", attr.get('href'))