from os import access
import selenium
from selenium import webdriver
#from selenium.webdriver import Firefox, Chrome, Edge
from selenium.webdriver.common.keys import Keys
import time
#not working ver
chrome_PATH = "chromedriver.exe" #for now just chrome web driver but for firefox e.g. similar setup . currently chrome v 90
driver = webdriver.Chrome(chrome_PATH) 

def test_login():
    driver.get("http://localhost:5000/login")   
    #works from here
    username = driver.find_element_by_id("username")
    password = driver.find_element_by_id("password")

    username.send_keys("jord")
    password.send_keys("jord")

    driver.find_element_by_id("submit").click()
    return

def access_lessons(): #testing lesson access with login/out
    test_login()
    driver.find_element_by_link_text("Begin Learning").click()
    driver.get("http://localhost:5000/lesson1")



    driver.find_element_by_link_text("Logout").click()
    driver.get("http://localhost:5000/Home")
    driver.find_element_by_link_text("Begin Learning").click()
    driver.get("http://localhost:5000/lesson1")

    return



def main():
    access_lessons()

    return

main()