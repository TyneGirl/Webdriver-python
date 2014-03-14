
#coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import os,time
import random
chromedriver="D:\Program Files (x86)\Chrome\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver) # Get local session of firefox
browser.maximize_window()
browser.get("http://192.168.1.20:9999") # Load page
def login():
    browser.find_element_by_id("txtAccount").send_keys("4@pc.com")
    time.sleep(2)
    log=browser.find_element_by_id("txtPwd")
    log.send_keys("123456" + Keys.RETURN)
login()
#def newproject():
time.sleep(2)
browser.find_element_by_xpath("//div[@class='pm tile double icon bg-color-blueLight']/div/img").click()  
time.sleep(2)
browser.find_element_by_xpath("//div[@id='content']/div[1]/div/div[7]/div[1]/a").click()
time.sleep(2)
browser.find_element_by_xpath("//html/body/div[2]/div[2]/ul/li[1]/a").click()
time.sleep(2)
browser.find_element_by_xpath("//html/body/div[2]/div[2]/ul/li[2]/a").click()
time.sleep(2)
browser.find_element_by_xpath("html/body/div[2]/div[2]/ul/li[3]/a").click()
time.sleep(2)
browser.find_element_by_xpath("html/body/div[2]/div[2]/ul/li[4]/a").click()
time.sleep(2)
browser.find_element_by_id("tasksLink").click()
time.sleep(2)
browser.find_element_by_id("locationLink").click()
time.sleep(2)
browser.find_element_by_id("surveyorCompanyLink").click()
time.sleep(2)
browser.find_element_by_xpath("html/body/div[1]/div/div[1]/a[2]").click()
time.sleep(2)
browser.find_element_by_xpath("html/body/div[1]/div/div[1]/a[3]").click()
time.sleep(2)
browser.find_element_by_xpath("html/body/div[1]/div/div[1]/a[4]").click()
print "ok"








