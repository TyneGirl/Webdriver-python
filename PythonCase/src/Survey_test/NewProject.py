#coding=utf-8
'''
Created on 2014��1��13��

@author: ting.liu
'''

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import os,time
import random
browser = webdriver.Ie() # Get local session of firefox
browser.maximize_window()
browser.get("http://192.168.1.20:9999") # Load page
def login():
    browser.find_element_by_id("txtAccount").send_keys("4@pc.com")
    log=browser.find_element_by_id("txtPwd")
    log.send_keys("123456" + Keys.RETURN)
#login()
def newproject():
    time.sleep(2)
    browser.find_element_by_xpath("//div[@class='pm tile double icon bg-color-blueLight']/div/img").click()  
    time.sleep(3)
    # browser.find_element_by_xpath("//div[@id='divbtn']").click()
    # time.sleep(3)
    browser.find_element_by_link_text("New Project").click()
    r=random.randint(1,1000)
    print r
    browser.find_element_by_id("projectName").send_keys(r)
    browser.find_element_by_id("clientId").click()
    time.sleep(2)
    m=browser.find_element_by_id("clientId")
    browser.implicitly_wait(10)
    m.find_elements_by_tag_name("option")[1].click()
    #m.find_element_by_xpath("//option[@value='e151ffe8-0824-45ee-9412-a0a8d13d2a12]").click()
    #browser.switch_to_frame("Index")
    #browser.find_element_by_id("clientId").find_elements_by_tag_name("option")[3].click()
    #browser.find_element_by_xpath("//select[@id='clientid']/option[4]").click()
    #browser.switch_to_alert().accept()
    #browser.switch_to_frame("Index")
    time.sleep(2)
    browser.find_element_by_id("finishData").click()
    print "w"
    time.sleep(2)
    browser.find_element_by_xpath("//div[@id='ui-datepicker-div']/table/tbody/tr[5]/td[2]/a").click()
    print"2"
    browser.find_element_by_xpath("//div[@id='createProject']/ul/li/div/div[4]/div").click()
    time.sleep(2)
    browser.find_element_by_id("project_locations.html").click()
    time.sleep(2)
    nowhandle=browser.current_window_handle
    
    #aalhandles=browser.window_handles()
    
    browser.find_element_by_id("btnAddLocation").click()
    print"ok"    
    #browser.switch_to_window(1)
    print "hello chenyun"
    #time.sleep(5)
    #browser.find_element_by_xpath("//div[@id='grid']/tbody/tr[2]/td/div/span").highlight
    #time.sleep(15)
    #browser.find_element_by_xpath("//div[@id='grid']/tbody/tr[2]/td/div/span").click()
    
    #browser.switch_to_window(browser.current_window_handle())
    
    
    win=browser.current_window_handle
    print "win==", win
    #     win01=browser.window_handles
    #     print"win01==", win01
    #browser.switch_to_window("Index")
    #browser.switch_to_window(handle)
    #aalhandles=browser.window_handles()
    #print len(aalhandles)
    #     for handle in browser.window_handles:
    #       if handle!=nowhandle:
    #          browser.switch_to_window(handle)
    #          browser.find_element_by_xpath("//div[@id='grid']/tbody/tr[2]/td/div/span").click()
    #          browser.find_element_by_xpath("//div[@id='outlist']/div/div[3]/div/table/thead/tr/th/div/span").click()
            #a= browser.find_element_by_xpath("//div[@id='grid']/tbody/tr[2]/td/div/span")
    #     time.sleep(2)
    #browser.find_element_by_xpath("//div[@id='grid']/tbody/tr[2]/td/div/span").click()
    #browser.switch_to_window(nowhandle)
    browser.implicitly_wait(15)
    browser.switch_to_window(browser.window_handles[-1])
    time.sleep(4)
    #browser.find_element_by_xpath("//div[@id='grid']/tbody/tr[2]/td/div/span").highlight
    browser.find_element_by_xpath("//div[@id='grid']/tbody/tr[2]/td/div/span").click()  #checkbox
    time.sleep(2)
    browser.find_element_by_id("btnSubmit").click()
    #browser.find_element_by_xpath("//div[@id='outlist']/div/div[3]/div/table/thead/tr/th/div/span").click()  #
        #browser.find_element_by_id("cb_000005a").highlight
       # time.sleep(20)
       # browser.find_element_by_id("cb_000005a").click()
    # browser.switch_to_default_content()
    browser.switch_to_window(nowhandle)
    time.sleep(2)
    #step 3
    browser.find_element_by_id("project_templates.html").click()
    time.sleep(2)
    browser.find_element_by_xpath("//div[@id='outlist']/div/div[3]/div/table/thead/tr/th/div/span").click() 
    print"test"
    browser.find_element_by_id("btnSelect").click()
    time.sleep(2)
    browser.switch_to_window(browser.window_handles[-1])
    time.sleep(3)
    browser.find_element_by_xpath("//div[@id='clientList']/div/div/input").click()
    browser.find_element_by_id("btnSelect").click()
    time.sleep(2)
    browser.switch_to_window(nowhandle)
    #step 4s
    time.sleep(2)
    browser.find_element_by_id("project_companies.html").click()
    time.sleep(2)
    browser.find_element_by_xpath("//div[@id='outlist']/div/div[3]/div/table/thead/tr/th/div/span").click() 
    browser.find_element_by_id("btnSelect").click()
    time.sleep(2)
    browser.switch_to_window(browser.window_handles[-1])
    time.sleep(5)
    browser.find_element_by_xpath("//ul[@id='clientList']/li/input").click()
    time.sleep(2)
    browser.find_element_by_xpath("//html/body/div[1]/div[3]/input").click()
    time.sleep(2)
    browser.switch_to_window(nowhandle)
    #step 5
    time.sleep(2)
    browser.find_element_by_id("project_confirmation.html").click()
    time.sleep(2)
    browser.find_element_by_id("send").click()
    time.sleep(2)
    browser.find_element_by_xpath("//div[@id='startDiv']/div[3]/a").click()
    print"done"
    alerttes=browser.switch_to_alert()
    #print alerttes.text()
    time.sleep(2)
    alerttes.accept()
    print "ok"

for i in range(10):
      login() 
      time.sleep(3)  
      newproject()
      browser.close()
      time.sleep(2)









                                                           
