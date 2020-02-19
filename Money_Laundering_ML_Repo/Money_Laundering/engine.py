import Money_Laundering_ML_Repo.Money_Laundering.businessLogic as mlbl
import pandas as pd

# get all titles
# get all  titles from 5 pages
allTitles1 = mlbl.getSearchResultTitle(ejURL="https://www.google.com/search?q=dsk+developers+ltd&oq=dsk+developers+ltd&aqs=chrome..69i57.10393j0j7&sourceid=chrome&ie=UTF-8", ejXPath='//div[@id="search"]//div[@class="r"]//a//cite')
allTitles2 = mlbl.getSearchResultTitle(ejURL="https://www.google.com/search?q=dsk+developers+ltd&sxsrf=ACYBGNQn-2TC1rAjySPaEqfmbT0PYP_TaA:1581828616895&ei=CMpIXuGkNvHjz7sPhq6Y6AU&start=10&sa=N&ved=2ahUKEwjhyLjmotXnAhXx8XMBHQYXBl0Q8tMDegQIDhAu&cshid=1581828673698172&biw=1366&bih=387", ejXPath='//div[@id="search"]//div[@class="r"]//a//cite')
allTitles3 = mlbl.getSearchResultTitle(ejURL="https://www.google.com/search?q=dsk+developers+ltd&sxsrf=ACYBGNTtgcWrGj00rldhaNMwjlMkoriRxQ:1581957064648&ei=yL9KXuKhJ-bcz7sP3LCRoAQ&start=20&sa=N&ved=2ahUKEwjipY2ngdnnAhVm7nMBHVxYBEQ4ChDy0wN6BAgMEDA&biw=1366&bih=375", ejXPath='//div[@id="search"]//div[@class="r"]//a//cite')
allTitles4 = mlbl.getSearchResultTitle(ejURL="https://www.google.com/search?q=dsk+developers+ltd&sxsrf=ACYBGNSXZgtKy6RrFnIACekhKSmQsxeviw:1581957100366&ei=7L9KXqb7FcbDz7sPreyTmAE&start=30&sa=N&ved=2ahUKEwimoZG4gdnnAhXG4XMBHS32BBM4FBDy0wN6BAgMEDI&biw=1366&bih=370", ejXPath='//div[@id="search"]//div[@class="r"]//a//cite')
allTitles5 = mlbl.getSearchResultTitle(ejURL="https://www.google.com/search?q=dsk+developers+ltd&sxsrf=ACYBGNRxl_DGZu6K2Z22RgMmqy-4GTETEA:1581957260480&ei=jMBKXtH5HN3Wz7sP4rK5uAE&start=40&sa=N&ved=2ahUKEwjR772EgtnnAhVd63MBHWJZDhc4HhDy0wN6BAgMEDQ&biw=1366&bih=216", ejXPath='//div[@id="search"]//div[@class="r"]//a//cite')
# concatenate all lists
allTitles = [*allTitles1, *allTitles2, *allTitles3, *allTitles4, *allTitles5]

print(" ===== count of all titles are =====", len(allTitles))
print(" ===== all titles are =====\n")
for i in range(len(allTitles)):
    print(allTitles[i].text)

# get all URL
# get page 5 URL
allLinks1 = mlbl.getSearchResultUrl(ejURL="https://www.google.com/search?q=dsk+developers+ltd&oq=dsk+developers+ltd&aqs=chrome..69i57.10393j0j7&sourceid=chrome&ie=UTF-8", ejXPath='//a/h3')
allLinks2 = mlbl.getSearchResultUrl(ejURL="https://www.google.com/search?q=dsk+developers+ltd&sxsrf=ACYBGNQn-2TC1rAjySPaEqfmbT0PYP_TaA:1581828616895&ei=CMpIXuGkNvHjz7sPhq6Y6AU&start=10&sa=N&ved=2ahUKEwjhyLjmotXnAhXx8XMBHQYXBl0Q8tMDegQIDhAu&cshid=1581828673698172&biw=1366&bih=387", ejXPath='//a/h3')
allLinks3 = mlbl.getSearchResultUrl(ejURL="https://www.google.com/search?q=dsk+developers+ltd&sxsrf=ACYBGNTtgcWrGj00rldhaNMwjlMkoriRxQ:1581957064648&ei=yL9KXuKhJ-bcz7sP3LCRoAQ&start=20&sa=N&ved=2ahUKEwjipY2ngdnnAhVm7nMBHVxYBEQ4ChDy0wN6BAgMEDA&biw=1366&bih=375", ejXPath='//a/h3')
allLinks4 = mlbl.getSearchResultUrl(ejURL="https://www.google.com/search?q=dsk+developers+ltd&sxsrf=ACYBGNSXZgtKy6RrFnIACekhKSmQsxeviw:1581957100366&ei=7L9KXqb7FcbDz7sPreyTmAE&start=30&sa=N&ved=2ahUKEwimoZG4gdnnAhXG4XMBHS32BBM4FBDy0wN6BAgMEDI&biw=1366&bih=370", ejXPath='//a/h3')
allLinks5 = mlbl.getSearchResultUrl(ejURL="https://www.google.com/search?q=dsk+developers+ltd&sxsrf=ACYBGNRxl_DGZu6K2Z22RgMmqy-4GTETEA:1581957260480&ei=jMBKXtH5HN3Wz7sP4rK5uAE&start=40&sa=N&ved=2ahUKEwjR772EgtnnAhVd63MBHWJZDhc4HhDy0wN6BAgMEDQ&biw=1366&bih=216", ejXPath='//a/h3')
# concatenate all lists
allLinks = [*allLinks1, *allLinks2, *allLinks3, *allLinks4, *allLinks5]
print(" ===== count of all URLs are =====", len(allLinks))
print(" ===== all URLs are =====\n")
for i in range(len(allLinks)):
    print(allLinks[i].text)

   # get all Text
   # get page 1 Text
   # //div[@class='s'] , //span[@class="st"]
allText1 = mlbl.getSearchResultText(ejURL="https://www.google.com/search?q=dsk+developers+ltd&oq=dsk+developers+ltd&aqs=chrome..69i57.10393j0j7&sourceid=chrome&ie=UTF-8",ejQSS="div > span[class='st']")
allText2 = mlbl.getSearchResultText(ejURL="https://www.google.com/search?q=dsk+developers+ltd&sxsrf=ACYBGNQn-2TC1rAjySPaEqfmbT0PYP_TaA:1581828616895&ei=CMpIXuGkNvHjz7sPhq6Y6AU&start=10&sa=N&ved=2ahUKEwjhyLjmotXnAhXx8XMBHQYXBl0Q8tMDegQIDhAu&cshid=1581828673698172&biw=1366&bih=387",ejQSS="div > span[class='st']")
allText3 = mlbl.getSearchResultText(ejURL="https://www.google.com/search?q=dsk+developers+ltd&sxsrf=ACYBGNTtgcWrGj00rldhaNMwjlMkoriRxQ:1581957064648&ei=yL9KXuKhJ-bcz7sP3LCRoAQ&start=20&sa=N&ved=2ahUKEwjipY2ngdnnAhVm7nMBHVxYBEQ4ChDy0wN6BAgMEDA&biw=1366&bih=375",ejQSS="div > span[class='st']")
allText4 = mlbl.getSearchResultText(ejURL="https://www.google.com/search?q=dsk+developers+ltd&sxsrf=ACYBGNSXZgtKy6RrFnIACekhKSmQsxeviw:1581957100366&ei=7L9KXqb7FcbDz7sPreyTmAE&start=30&sa=N&ved=2ahUKEwimoZG4gdnnAhXG4XMBHS32BBM4FBDy0wN6BAgMEDI&biw=1366&bih=370",ejQSS="div > span[class='st']")
allText5 = mlbl.getSearchResultText(ejURL="https://www.google.com/search?q=dsk+developers+ltd&sxsrf=ACYBGNRxl_DGZu6K2Z22RgMmqy-4GTETEA:1581957260480&ei=jMBKXtH5HN3Wz7sP4rK5uAE&start=40&sa=N&ved=2ahUKEwjR772EgtnnAhVd63MBHWJZDhc4HhDy0wN6BAgMEDQ&biw=1366&bih=216",ejQSS="div > span[class='st']")
# concatenate all text lists
allText = [*allText1, *allText2, *allText3, *allText4, *allText5]
print(" ===== count of all texts are =====", len(allText))
print(" ===== all texts are =====\n")
for i in range(len(allText)):
    print(allText[i].text)



# storing titles and links in dataframe.
#df = pd.DataFrame(allTitles.text)
#df = pd.DataFrame({'AllTitles':allTitles,'AllLinks':allLinks})
#print(" ===== printing data frame =====\n")
#print(df)
#df.to_csv('products.csv', index=False, encoding='utf-8')


# get all Text
# get page 1 Text
# //div[@class='s'] , //span[@class="st"]
# allText = mlbl.getSearchResultText(ejURL="https://www.google.com/search?q=dsk+developers+ltd&oq=dsk+developers+ltd&aqs=chrome..69i57.10393j0j7&sourceid=chrome&ie=UTF-8",ejXPath='//div[@class="s"]')
# print(" ===== count of all texts are =====", len(allText))
# print(" ===== all texts are =====\n")
# for i in range(len(allText)):
#     print(allText[i].text)



