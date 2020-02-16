import GFL.ejWebOperations as ejwb

driver=ejwb.ejWebOperations(ejShowBrowser=True, ejChromeDriverExePath="D:\Data Science\Manish_Sir_class\MoneyLaundering_ML_Proj\Drivers\chromedriver.exe")
var=driver.getPageSource(ejURL="www.google.com/search?q=dsk+developers+ltd&oq=dsk+developers+ltd&aqs=chrome..69i57.10393j0j7&sourceid=chrome&ie=UTF-8")
#print("=====page content====== ",var)

allTitles = driver.getWebElements(ejXPath='//div[@id="search"]//div[@class="r"]//a//cite')
print("======= total titles count on page === ", len(allTitles))

# all titles - //div[@id='search']//div[@class='r']//a//cite
for i in range(len(allTitles)):
    print(allTitles[i].text)