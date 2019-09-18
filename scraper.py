#
#
#
# from nd_county_webscraper.core.run_state import RunState
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from datetime import datetime, timedelta
# import os
# from time import sleep
#
#
# def main():
#     # chrome_options = webdriver.ChromeOptions()
#     # chrome_options.add_argument('--no-sandbox')
#     # chrome_options.add_argument('--disable-web-security')
#     # chrome_options.add_argument('--safebrowsing-disable-download-protection')
#     # driver = webdriver.Chrome(chrome_options=chrome_options)
#     # driver_path =os.path.join(os.getcwd(),"driver","chromedriver.exe")
#     # print(driver_path)
#     driver = webdriver.Chrome()
#     # start_date = datetime.today() - timedelta(days=30)
#     # start_date = ('12/18/2017').strftime('%m/%d/%Y')
#     start_date = '04/01/2015'
#     print(start_date)
#     end_date = datetime.today()
#     end_date = end_date.strftime('%m/%d/%Y')
#     print(end_date)
#     url = r"https://www.idocmarket.com/Security/Register"
#     # uid = r"stephen.langford@drillinginfo.com"
#     # pwd = r"Leasingland@2"
#     instrument_types = ['LEASE','2ND COR OF OGL & MEMO OGL','ABSTRACT OF OIL & GAS LEASE',"ACT OF CORRECTION","ADDENDUM TO OIL & GAS LEASE"]
#
#
#
#     driver.get(url)
#
#     try:
#         username = driver.find_element_by_id("Login_Username")
#         username.send_keys("stephen.langford@drillinginfo.com")
#         password = driver.find_element_by_id("Login_Password")
#         password.send_keys("Leasingland@2")
#         # sleep(10)
#         # login2 = driver.find_element_by_name('Login')
#         login= driver.find_element_by_xpath("//*[@id='loginForm']/div[5]/button[1]")
#         # login    = driver.find_element_by_class_name("btn btn-primary")
#         login.click()
#         sleep(5)
#         subscribed_county_list = []
#         hRefs=[]
#
#         elements = driver.find_elements_by_xpath("// *[ @ id = 'master-container'] / div / div[2]/div")
#         for element in elements:
#             subscribed_county_list=[x.text for x in element.find_elements_by_tag_name("h4")]
#             links = element.find_elements_by_partial_link_text('Search')
#             for link in links:
#                 hRefs.append(link.get_attribute('href'))
#                 link.click()
#                 sleep(10)
#                 rec_startdate = driver.find_element_by_id('StartRecordDate')
#                 rec_enddate = driver.find_element_by_id('EndRecordDate')
#                 rec_startdate.click()
#                 rec_startdate.send_keys(start_date)
#                 rec_enddate.click()
#                 rec_enddate.send_keys(end_date)
#
#
#                 for opt in instrument_types:
#                     ins_types = Select(driver.find_element_by_id('Instrument'))
#                     print(opt)
#                     try:
#                         ins_types.select_by_value(opt)
#                         sleep(10)
#                         # driver.find_element_by_class_name('btn btn-primary').click()
#                         driver.find_element_by_css_selector(".btn-primary").click() #Search Button Click
#                         sleep(10)
#
#                         # row_items = driver.find_elements_by_xpath('//div[@class="result-item"]')
#                         row_items = len(driver.find_elements_by_class_name('result-item'))
#                         try:
#                             # for i, row in enumerate(row_items, 1):
#                             for row in range(row_items):
#                                 print(row)
#                                 try:
#                                     print(driver.find_element_by_class_name(' btn-stacked'))
#                                     driver.find_elements_by_class_name(' btn-stacked')[row].click() #'View' Button Click
#                                     sleep(10)
#                                     link=driver.find_element_by_class_name(' btn-primary') # 'Back' Button
#                                     sleep(5)
#                                     link.click()
#                                 except Exception as e:
#                                     print(e)
#                         except Exception as e:
#                             print(e)
#
#                             # link = row.find_element_by_tag_name("a")
#                             # link.get_attribute("href")
#                             # link.click()
#                             # driver.find_element_by_class_name(' btn-primary').click()
#                             # print(i)
#
#
#                             # try:
#                             #     print(row.text)
#                             #     print(row.find_element_by_tag_name("a"))
#                             #     link= row.find_element_by_tag_name("a")
#                             #     link.get_attribute("href")
#                             #     link.click()              #'View' button click
#                             #     sleep(5)
#                             #     driver.find_element_by_class_name(' btn-primary').click()    #'back' button click
#                             #     sleep(10)
#                             # except Exception as e:
#                             #     print(e)
#                             #     continue
#                     except Exception as e:
#                      print(e)
#
#     except Exception as e:
#         print(e)
#
# # //*[@id="Doc:7f31MrxGPkw="]/div[5]
# # //*[@id="Doc:7f31MrxGPkw="]/div[5]/a
# main()







# McKenzie is county in North Dakota.

from selenium import webdriver
from selenium.webdriver.support.select import Select
from datetime import datetime, timedelta
import os
from time import sleep
#
# def main():
#     url = "http://www.mcvvault.com/"
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(20)
#     driver.get(url)
#     email_id="stephen.langford@drillinginfo.com"
#     pwd="Leasingland@1"
#
#     driver.find_element_by_id("login").click()  # Click on Member Login
#     email = driver.find_element_by_id("Email")
#     email.send_keys(email_id)  # enter email address
#     password = driver.find_element_by_id("Password")
#     password.send_keys(pwd)  # enter password
#     login = driver.find_element_by_xpath("//*[ @ id = 'loginForm'] / form / div[4] / div / input")
#     login.click()
#     sleep(10)
#
#
#     link = driver.find_element_by_link_text('Real Estate Documents')
#     link.click()
#
#     driver.close()
#
# main()


list = ["javascript:viewDoc('7f31MrxGPkw%3d' );", "javascript:viewDoc('bSzlN2joRZQ%3d' );",
        "javascript:viewDoc('wnpu1V8rQKs%3d' );","javascript:viewDoc('nwSkFtr6v%7bplus%7dQ%3d' );"]

import re

txt='"javascript:viewDoc(\'7f31MrxGPkw%3d\' );", "javascript:viewDoc(\'bSzlN2joRZQ%3d\' );", "javascript:viewDoc(\'wnpu1V8rQKs%3d\')'

#txt = ["javascript:viewDoc('7f31MrxGPkw%3d' );", "javascript:viewDoc('bSzlN2joRZQ%3d' );",
#        "javascript:viewDoc('wnpu1V8rQKs%3d' );","javascript:viewDoc('nwSkFtr6v%7bplus%7dQ%3d' );"]

re1='.*?'	# Non-greedy match on filler
re2='(\\\'.*?\\\')'	# Single Quote String 1
re3='.*?'	# Non-greedy match on filler
re4='(\\\'.*?\\\')'	# Single Quote String 2
re5='.*?'	# Non-greedy match on filler
re6='(\\\'.*?\\\')'	# Single Quote String 3

rg = re.compile(re1+re2+re3+re4+re5+re6,re.IGNORECASE|re.DOTALL)
m = rg.search(txt)
if m:
    strng1=m.group(1)
    strng2=m.group(2)
    strng3=m.group(3)
    print("("+strng1+")"+"("+strng2+")"+"("+strng3+")"+"\n")

