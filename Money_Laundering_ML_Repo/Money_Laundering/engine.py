import Money_Laundering.businessLogic as mlbl

# get all titles
# get page 1 titles
allTitles = mlbl.getSearchResultTitle(ejURL="https://www.google.com/search?q=dsk+developers+ltd&oq=dsk+developers+ltd&aqs=chrome..69i57.10393j0j7&sourceid=chrome&ie=UTF-8", ejXPath='//div[@id="search"]//div[@class="r"]//a//cite')
print(" ===== count of all titles are =====", len(allTitles))
print(" ===== all titles are =====\n")
for i in range(len(allTitles)):
    print(allTitles[i].text)

    # https://www.google.com/search?q=dsk+developers+ltd&sxsrf=ACYBGNQn-2TC1rAjySPaEqfmbT0PYP_TaA:1581828616895&ei=CMpIXuGkNvHjz7sPhq6Y6AU&start=10&sa=N&ved=2ahUKEwjhyLjmotXnAhXx8XMBHQYXBl0Q8tMDegQIDhAu&cshid=1581828673698172&biw=1366&bih=387

# get all titles page 2
# get page 2 titles
allTitles2 = mlbl.getSearchResultTitle(ejURL="https://www.google.com/search?q=dsk+developers+ltd&sxsrf=ACYBGNQn-2TC1rAjySPaEqfmbT0PYP_TaA:1581828616895&ei=CMpIXuGkNvHjz7sPhq6Y6AU&start=10&sa=N&ved=2ahUKEwjhyLjmotXnAhXx8XMBHQYXBl0Q8tMDegQIDhAu&cshid=1581828673698172&biw=1366&bih=387", ejXPath='//div[@id="search"]//div[@class="r"]//a//cite')
print(" ===== count of all titles are =====", len(allTitles2))
print(" ===== all titles on page 2 are =====\n")
for i in range(len(allTitles2)):
    print(allTitles2[i].text)

# get all URL
# get page 1 URL
allLinks = mlbl.getSearchResultUrl(ejURL="https://www.google.com/search?q=dsk+developers+ltd&oq=dsk+developers+ltd&aqs=chrome..69i57.10393j0j7&sourceid=chrome&ie=UTF-8", ejXPath='//a/h3')
print(" ===== count of all URLs are =====", len(allLinks))
print(" ===== all URLs are =====\n")
for i in range(len(allLinks)):
    print(allLinks[i].text)

# get all Text
# get page 1 Text
# //div[@class='s'] , //span[@class="st"]
allText = mlbl.getSearchResultText(ejURL="https://www.google.com/search?q=dsk+developers+ltd&oq=dsk+developers+ltd&aqs=chrome..69i57.10393j0j7&sourceid=chrome&ie=UTF-8",ejXPath='//div[@class="s"]')
print(" ===== count of all texts are =====", len(allText))
print(" ===== all texts are =====\n")
for i in range(len(allText)):
    print(allText[i].text)



