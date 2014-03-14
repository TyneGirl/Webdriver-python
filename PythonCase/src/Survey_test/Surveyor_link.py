#coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import os,time
import random
chromedriver="D:\Program Files (x86)\Chrome\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)
browser.maximize_window()
browser.get("http://192.168.1.20:9999") # Load page
def login():
    browser.find_element_by_id("txtAccount").send_keys("tingting008_2013@126.com")
    log=browser.find_element_by_id("txtPwd")
    log.send_keys("123456" + Keys.RETURN)

login()
time.sleep(2)
#task detail page
browser.find_element_by_xpath("//div[@id='content']/div/div[3]/dl/dd[4]/a").click()
time.sleep(2)
browser.find_element_by_xpath("//div[@id='PhotoGalleryWrap']/div[2]/div/dl/dt/a/img").click()
time.sleep(3)
browser.find_element_by_xpath("//a[@id='lightbox-secNav-btnTransform']/img").click()
time.sleep(2)
browser.find_element_by_id("editPhotoBtn").click()
time.sleep(2)
browser.find_element_by_id("lightbox-image-details-caption").clear()
time.sleep(2)
browser.find_element_by_id("lightbox-image-details-caption").send_keys("selenium test001")
time.sleep(2)
browser.find_element_by_id("savePhotoBtn").click()
time.sleep(2)
browser.find_element_by_xpath("//a[@id='lightbox-secNav-btnTransform']/img")
time.sleep(2)
browser.find_element_by_xpath("//a[@id='lightbox-secNav-btnClose']/img").click()
print"ok"
browser.find_element_by_id("txtComment").send_keys("selenium test if-auto test")
time.sleep(2)
browser.find_element_by_id("btnAddComment").click()
#all task page
browser.find_element_by_xpath("html/body/div[1]/div[2]/div/div[1]/a[1]").click()
time.sleep(2)
browser.find_element_by_xpath("html/body/div[2]/div[1]/div[1]/div[3]/a").click()
time.sleep(2)
browser.find_element_by_xpath("//div[@id='grid']/tbody/tr[1]/td[1]/div").click()
time.sleep(2)
#browser.find_element_by_xpath("//div[@id='InProgress_Template']/div[3]/a").click()
browser.find_element_by_xpath("html/body/div[1]/div[2]/div/div[1]/a[2]").click()
time.sleep(3)
browser.find_element_by_xpath("//div[@id='content']/div/div[5]/div/tbody/tr/td/div").click()
# browser.find_element_by_xpath("div[@id='grid']/tbody/tr/td/div").click()
time.sleep(2)
#schedule the task
browser.find_element_by_id("btnScheduled").click()
time.sleep(2)
browser.find_element_by_xpath("//div[@id='timechoose_confirm']/a").click()
alerttes=browser.switch_to_alert()
#print alerttes.text()
print "test"
alerttes.accept()
#alert.dismiss()
time.sleep(2)
test=browser.switch_to_alert()
time.sleep(2)
test.accept()
time.sleep(2)
browser.find_element_by_xpath("//div[@id='grid']/tbody/tr[1]/td[1]/div").click()
browser.quit()











