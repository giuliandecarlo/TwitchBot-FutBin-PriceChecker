from queue import Empty
from bs4 import BeautifulSoup
from selenium import webdriver

def searchPlayer(searchKey):   #function that searches for the SearchKey on futbin and builds the response message
    try:
        driver=webdriver.Firefox(executable_path='files/geckodriver')
        if(" "in searchKey):
            searchKey=searchKey.replace(" ","%20")
        driver.get('https://www.futbin.com/players?page=1&search='+searchKey)

        html=driver.page_source
        soup =BeautifulSoup(html,features="html.parser")
        prices= soup.findAll("span",{"class":"ps4_color font-weight-bold"})
        types= soup.findAll("td",{"class":"mobile-hide-table-col"})
        names=soup.findAll("div",{"class":"d-inline pt-2 pl-3"})
        messageRet=""

        for i in range(len(prices)):
            typeMess=types[i].text.split()
            namesElenc=names[i].text.split()
            totalMess=""
            totalName=""

            for word in typeMess:
                totalMess=totalMess+" "+word

            for wordName in namesElenc:
                totalName=totalName+" "+wordName
            messageRet=messageRet+(":heavy_minus_sign:👤"+totalName+"["+totalMess+"]:"+prices[i].text)

        driver.quit()
        if(len(messageRet)>500 or messageRet==""):  #twitch chats have a 500 character limit
            return("There was an error, the search did not give any results or the result was too long")
        return(":heavy_minus_sign: "+":heavy_minus_sign: "+":heavy_minus_sign: "+":heavy_minus_sign: "+":heavy_minus_sign: "+":heavy_minus_sign: "+messageRet)
    except:
        return("An error has occurred, please try again")