from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

url = 'https://www.programmableweb.com/apis/directory'

response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
time.sleep(5)

# apiNames = soup.find_all("td", {"class":"views-field-title"})
# for name in apiNames:
#     print(name.text)

table = soup.find("table", {"class":"views-table"})
tbody = table.find("tbody")

rows = tbody.find_all("tr")
print(len(rows))
for row in range(0,len(rows)):
    apiName = rows[row].find("td",{"class":"views-field-title"})
    description = rows[row].find("td", {"class":"views-field-field-api-description"})
    category = rows[row].find("td", {"class":"views-field-field-article-primary-category"})
    print(apiName)
    print(description)
    print(category)

