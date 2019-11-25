from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import pandas as pd

driver = webdriver.Chrome('C:/Users/akhila.vemuganti/Downloads/chromedriver_win32/chromedriver.exe')
driver.maximize_window()

url = 'https://www.programmableweb.com/apis/directory'

api_dict={}
apiCount=0
while True:
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')

    driver.get(url)
    time.sleep(5)

    rows = soup.find_all("tr",{"class":['even','odd']})
    print(len(rows))
    for row in range(0,len(rows)):
        apiName = rows[row].find("td",{"class":"views-field-title"}).text
        path=rows[row].find("a").get('href')
        absoluteURL = 'https://www.programmableweb.com' +path
        category_tag = rows[row].find("td", {"class":"views-field-field-article-primary-category"})
        category = category_tag.text if category_tag else "N/A"
        description = rows[row].find("td", {"class": "views-field-field-api-description"}).text

        apiCount+=1
        api_dict[apiCount]=[apiName,absoluteURL,category,description]
        print("APIName: "+apiName)
        print("URL: "+absoluteURL)
        print("Description: "+description)
        print("Category: "+category)
        print ("-----------------------------------------------------------------------------------")
    url_tag=soup.find("a",{"title":"Go to next page"})
    if url_tag.get('href'):
        url = "https://www.programmableweb.com"+url_tag.get('href')
        print(url)
    else:
        print("No Next")
        break
print (apiCount)
api_df = pd.DataFrame.from_dict(api_dict,orient='index',columns=["API Name","Absolute URL","Category","Description"])
api_df.to_csv("API_Names.csv")
# driver.close()