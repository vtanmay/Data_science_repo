from lxml import etree

import Money_Laundering_ML_Repo.Money_Laundering.businessLogic as mlbl
import pandas as pd
# what is python  dsk+developers+ltd
# //*[@id="rso"]/div/div/div[1]/div/div/div[2]/div/span
titleList=[]
linkList = []
textList = []
# get all titles
# get all  titles from 5 pages
allTitles1 = mlbl.getSearchResultTitle(ejURL="https://www.google.com/search?q=dsk+developers+ltd", ejXPath='//div[@id="search"]//div[@class="r"]//a//cite')
# for i in range(len(allTitles1)):
#     print(allTitles1[i].text)
    #titleList.append(allTitles[i].text)
allTitles2 = mlbl.getSearchResultTitle(ejURL="https://www.google.com/search?q=dsk+developers+ltd&start=10", ejXPath='//div[@id="search"]//div[@class="r"]//a//cite')
allTitles3 = mlbl.getSearchResultTitle(ejURL="https://www.google.com/search?q=dsk+developers+ltd&start=20", ejXPath='//div[@id="search"]//div[@class="r"]//a//cite')
allTitles4 = mlbl.getSearchResultTitle(ejURL="https://www.google.com/search?q=dsk+developers+ltd&start=30", ejXPath='//div[@id="search"]//div[@class="r"]//a//cite')
allTitles5 = mlbl.getSearchResultTitle(ejURL="https://www.google.com/search?q=dsk+developers+ltd&start=40", ejXPath='//div[@id="search"]//div[@class="r"]//a//cite')
# concatenate all lists
allTitles = [*allTitles1, *allTitles2, *allTitles3, *allTitles4, *allTitles5]

print(" ===== count of all titles are =====", len(allTitles))
print(" ===== all titles are =====\n")
for i in range(len(allTitles)):
    print(allTitles[i].text)
    titleList.append(allTitles[i].text)

# get all URL
# get page 5 URL
allLinks1 = mlbl.getSearchResultUrl(ejURL="https://www.google.com/search?q=dsk+developers+ltd", ejXPath='//a/h3')
allLinks2 = mlbl.getSearchResultUrl(ejURL="https://www.google.com/search?q=dsk+developers+ltd&start=10", ejXPath='//a/h3')
allLinks3 = mlbl.getSearchResultUrl(ejURL="https://www.google.com/search?q=dsk+developers+ltd&start=20", ejXPath='//a/h3')
allLinks4 = mlbl.getSearchResultUrl(ejURL="https://www.google.com/search?q=dsk+developers+ltd&start=30", ejXPath='//a/h3')
allLinks5 = mlbl.getSearchResultUrl(ejURL="https://www.google.com/search?q=dsk+developers+ltd&start=40", ejXPath='//a/h3')
# concatenate all lists
allLinks = [*allLinks1, *allLinks2, *allLinks3, *allLinks4, *allLinks5]
print(" ===== count of all URLs are =====", len(allLinks))
print(" ===== all URLs are =====\n")
for i in range(len(allLinks)):
    print(allLinks[i].text)
    linkList.append(allLinks[i].text)

   # get all Text
   # get page 1 Text
   # ejQSS="div > span[class='st']"
   # //div[@class='s'] , //span[@class="st"]
allText1 = mlbl.getSearchResultText(ejURL="https://www.google.com/search?q=dsk+developers+ltd",ejXPath='//div/div[@class="rc"]/div/div/span')
allText2 = mlbl.getSearchResultText(ejURL="https://www.google.com/search?q=dsk+developers+ltd&start=10",ejXPath='//div/div[@class="rc"]/div/div/span')
allText3 = mlbl.getSearchResultText(ejURL="https://www.google.com/search?q=dsk+developers+ltd&start=20",ejXPath='//div/div[@class="rc"]/div/div/span')
allText4 = mlbl.getSearchResultText(ejURL="https://www.google.com/search?q=dsk+developers+ltd&start=30",ejXPath='//div/div[@class="rc"]/div/div/span')
allText5 = mlbl.getSearchResultText(ejURL="https://www.google.com/search?q=dsk+developers+ltd&start=40",ejXPath='//div/div[@class="rc"]/div/div/span')
# concatenate all text lists
allText = [*allText1, *allText2, *allText3, *allText4, *allText5]
print(" ===== count of all texts are =====", len(allText))
print(" ===== all texts are =====\n")
for i in range(len(allText)):
    print(etree.tostring(allText[i],encoding=str,method="text"))
    #textList.append(allText[i].text)

# Add list to data frame
# df = pd.DataFrame({'Titles': titleList, 'Links': linkList, 'Text': textList})
# df = df.replace({r'\s+$': '', r'^\s+': ''}, regex=True).replace(r'\n',  ' ', regex=True)
#
# print("------Titles------",df['Titles'])
# print("------Links------",df['Links'])
# print("------Text------",df['Text'])

# dumping data into CSV.
#df.to_csv('dskDeveloperInfo.csv', index=False, encoding='utf-8')



