#coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import os,time
import random
browser = webdriver.Firefox() # Get local session of firefox
browser.maximize_window()
browser.get("http://192.168.1.20:9999") # Load page
def login():
    browser.find_element_by_id("txtAccount").send_keys("tingting008_2013@126.com")
    log=browser.find_element_by_id("txtPwd")
    log.send_keys("123456" + Keys.RETURN)

login()
time.sleep(2)
browser.find_element_by_link_text("Find Task").click()
time.sleep(2)
browser.find_element_by_xpath("//div[@id='content']/div/div[5]/div/tbody/tr/td/div").click()
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
browser.find_element_by_link_text("My Task").click()
time.sleep(2)
browser.find_element_by_xpath("//div[@id='content']/div/div[3]/dl/dd[4]/a").click()
time.sleep(2)
  #  browser.find_element_by_id("gallery-btnUploadPhoto").click()
  #  time.sleep(1)
  #  browser.switch_to_frame("gallery-uploadPhotoAreaFrame")
   # time.sleep(2)
 #   browser.find_element_by_id("SWFUpload_0").click()
 #   print"ok"
  #  browser.implicitly_wait(10)
    #browser.find_element_by_id("SWFUpload_0").send_keys('F:\ting.liu\PICTURE\2.jpg'+ Keys.RETURN)
   # browser.find_element_by_id("SWFUpload_0").send_keys("D:\2.jpg")
   # print"123"
  #  browser.find_element_by_xpath("//body/div/div[2]/div/div[4]/ul/li/a/img").click()
    #print "test"
browser.find_element_by_xpath("//div[@id='surveyItemsWrap']/div[1]/div[2]/button").click()
time.sleep(2)
browser.find_element_by_xpath("//div[@id='surveyItemsWrap']/div[2]/div/div[2]/div[2]/div[2]/div/span[2]/select").click()
time.sleep(2)
se=browser.find_element_by_xpath("//div[@id='surveyItemsWrap']/div[2]/div/div[2]/div[2]/div[2]/div/span[2]/select")
se.find_elements_by_tag_name("option")[2].click()
time.sleep(2)
browser.find_element_by_xpath("//div[@id='surveyItemsWrap']/div[2]/div/div[2]/div[3]/div[2]/div/span[2]/select").click()
se02=browser.find_element_by_xpath("//div[@id='surveyItemsWrap']/div[2]/div/div[2]/div[3]/div[2]/div/span[2]/select")
time.sleep(2)
se02.find_elements_by_tag_name("option")[1].click()
time.sleep(2)
browser.find_element_by_xpath("//div[@id='surveyItemsWrap']/div[1]/div[2]/button[2]").click()
time.sleep(2)
browser.find_element_by_id("btnSubmitInprogress").click()
time.sleep(2)
print "done"
test01=browser.switch_to_alert()
time.sleep(2)
test01.accept()
print "sucessfully scheduled"
browser.quit()












