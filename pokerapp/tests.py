import selenium
from selenium import webdriver
#from selenium.webdriver import Firefox, Chrome, Edge
from selenium.webdriver.common.keys import Keys
import time
#not working ver
chrome_PATH = "chromedriver.exe" #for now just chrome web driver but for firefox e.g. similar setup . currently chrome v 90
driver = webdriver.Chrome(chrome_PATH) 

driver.get("http://localhost:5000/login")
username = driver.find_element_by_id("Username")
password = driver.find_element_by_id("Password")

username.send_keys("jord")
password.send_keys("jord")

link = driver.find_element_by_link_text("Sign In")
link.click()
time.sleep(10)
driver.quit()
