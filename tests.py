from os import access
import selenium
from selenium import webdriver
#from selenium.webdriver import Firefox, Chrome, Edge
from selenium.webdriver.common.keys import Keys
import time

#To Begin Tests, run python file in terminal

#Currently selenium chrome tests only
chrome_PATH = "chromedriver.exe" #currently chrome v 90
#edge_PATH similar use for other browsers.

driver = webdriver.Chrome(chrome_PATH) 

def test_login(): #auto login
    driver.get("http://localhost:5000/login")   
    username = driver.find_element_by_id("username") #find login fields
    password = driver.find_element_by_id("password")

    username.send_keys("jord") #input login info
    password.send_keys("jord")

    driver.find_element_by_id("submit").click()
    return

def access_lessons(): #testing lesson access with login/out
    test_login() #Test lesson access when logged in
    driver.find_element_by_link_text("Begin Learning").click()
    driver.get("http://localhost:5000/lesson1")


    #test login access when logged out
    driver.find_element_by_link_text("Logout").click()
    driver.get("http://localhost:5000/Home")
    driver.find_element_by_link_text("Begin Learning").click()
    driver.get("http://localhost:5000/lesson1")
    #driver.quit()

    return



def main():
    access_lessons() #Test loggedin/out lesson access
    #see readme for info about other tests
    #Wait then close
    time.sleep(20)
    driver.quit()
    return

main()