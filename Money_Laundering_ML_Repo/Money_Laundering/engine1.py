import Money_Laundering_ML_Repo.Money_Laundering.businessLogic as mlbl
import pandas as pd

TitleList=[]
LinkList = []
TextList = []

allTitles = mlbl.getSearchResultTitle(ejURL="https://www.google.com/search?q=dsk+developers+ltd&oq=dsk+developers+ltd&aqs=chrome..69i57.10393j0j7&sourceid=chrome&ie=UTF-8", ejXPath='//div[@id="search"]//div[@class="r"]//a//cite')
print("Title Count :-", len(allTitles))
print("Title list :: ->")
for i in range(len(allTitles)):
    print(allTitles[i].text)
    TitleList.append(allTitles[i].text)

allLinks = mlbl.getSearchResultUrl(ejURL="https://www.google.com/search?q=dsk+developers+ltd&oq=dsk+developers+ltd&aqs=chrome..69i57.10393j0j7&sourceid=chrome&ie=UTF-8", ejXPath='//a/h3')
print("Link Count :-", len(allLinks))
print("Link list :: ->")
for i in range(len(allLinks)):
    print(allLinks[i].text)
    LinkList.append(allLinks[i].text)

allText = mlbl.getSearchResultText(ejURL="https://www.google.com/search?q=dsk+developers+ltd&oq=dsk+developers+ltd&aqs=chrome..69i57.10393j0j7&sourceid=chrome&ie=UTF-8",ejQSS="div > span[class='st']")
print("Text Count :-", len(allText))
print("Searched text list :-")
for i in range(len(allText)):
    print(allText[i].text)
    TextList.append(allText[i].text)

# Add list to dataframe
df = pd.DataFrame({'Titles': TitleList, 'Links': LinkList, 'Text': TextList})
df = df.replace({r'\s+$': '', r'^\s+': ''}, regex=True).replace(r'\n',  ' ', regex=True)

print("------Titles------",df['Titles'])
print("------Links------",df['Links'])
print("------Text------",df['Text'])

print("***********************************************************")
print("----Top 5 data-----",df.head())
df.to_csv('dskDeveloperInfo.csv', index=False, encoding='utf-8')



