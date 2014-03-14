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
chromedriver="D:\Program Files (x86)\Chrome\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver) # Get local session of firefox
browser.maximize_window()
browser.get("http://192.168.1.20:9999") # Load page
def login(accout):
    browser.find_element_by_id("txtAccount").send_keys(accout)
    log=browser.find_element_by_id("txtPwd")
    log.send_keys("123456" + Keys.RETURN)
def newaffi(name):
    browser.find_element_by_xpath("//ul[@id='menu']/li[2]/a").click()
    time.sleep(1)
    browser.find_element_by_id("btnNewAffiliate").click()
    browser.find_element_by_id("Name").send_keys(name)
    time.sleep(1)
    browser.find_element_by_xpath("//div[@id='EntityType']/div[1]").click()
    time.sleep(1)
    browser.find_element_by_xpath("//div[@id='EntityType']/div[2]/ul/li[3]").click()
    time.sleep(1)
    browser.find_element_by_xpath("//div[@id='StateRegistered']/div[1]").click()
    time.sleep(1)
    browser.find_element_by_xpath("//div[@id='StateRegistered']/div[2]/ul/li[8]").click()
    browser.find_element_by_id("Phone_1").send_keys("456")
    browser.find_element_by_id("Phone_2").send_keys("496")
    browser.find_element_by_id("Phone_3").send_keys("9820")
    browser.find_element_by_id("Phone_4").send_keys("9301")
    browser.find_element_by_id("Address_AddressLine1").send_keys("seleniumaddr")
    browser.find_element_by_id("Address_City").send_keys("seleniumcity")
    browser.find_element_by_id("Address_Zipcode").send_keys("12345")
    browser.find_element_by_xpath("//div[@id='Address_State']/div[1]/input[1]").click()
    time.sleep(1)
    browser.find_element_by_xpath("//div[@id='Address_State']/div[2]/ul/li[3]").click()
    browser.find_element_by_id("Address_Country").send_keys("China")
    time.sleep(1)
    browser.find_element_by_id("copyAddress").click()
    browser.find_element_by_id("MBECertified_CheckApplicable").click()
    time.sleep(1)
    browser.find_element_by_id("MBECertified_IsProve").click()
    time.sleep(2)
    browser.find_element_by_xpath("//body/input").send_keys('d:\\affiliate paperwork\ExhibitA.docx' )
    time.sleep(3)
    browser.find_element_by_id("SelfPerformingCrews").send_keys("5")
    browser.find_element_by_id("SubContractedCrews").send_keys("5")
    time.sleep(2)
    browser.find_element_by_xpath("//div[@id='ContactList']/div/div[2]/ul/li/div/input").send_keys("tyentest")
    browser.find_element_by_xpath("//div[@id='ContactList']/div/div[2]/ul[2]/li/div/input").send_keys("tyentest")
    browser.find_element_by_xpath("//div[@id='ContactList']/div/div[2]/ul[2]/li[3]/div/input[2]").send_keys("128")
    browser.find_element_by_xpath("//div[@id='ContactList']/div/div[2]/ul[2]/li[3]/div/input[3]").send_keys("129")
    browser.find_element_by_xpath("//div[@id='ContactList']/div/div[2]/ul[2]/li[3]/div/input[4]").send_keys("1223")
    time.sleep(2)
    browser.find_element_by_xpath("//div[@id='ServiceTypes']/div[1]/input[1]").click()
    time.sleep(2)
    browser.find_element_by_xpath("//div[@id='ServiceTypes']/div[2]/ul/li[2]").click()
    time.sleep(2)
    browser.find_element_by_xpath("//ul[@id='Services']/li/div/p/span").click()
    time.sleep(2)
    browser.find_element_by_xpath("//div[@id='btnAddService']/a").click()
    time.sleep(2)
    browser.find_element_by_id("ServicesEquipment").send_keys("selenium test")
    browser.find_element_by_xpath("//div[@id='ServiceAreas']/div/div[2]/div/div[3]/ul/li/div/input").send_keys("12345")
    browser.find_element_by_xpath("//div[@id='ServiceAreas']/div/div[2]/div/div[4]/ul/li/div/input").send_keys("12")
    time.sleep(2)
    browser.find_element_by_xpath("//html/body/div[3]/form/div[4]/button[1]").click()
    time.sleep(2)
    print"done"
    browser.find_element_by_xpath("//ul[@id='subMenu']/li[2]/a").click()
    time.sleep(2)
    browser.find_element_by_id("btnAssignCA").click()
    time.sleep(2)
    browser.find_element_by_xpath("//div[@id='selCA']/div[1]").click()
    time.sleep(2)
    browser.find_element_by_xpath("//div[@id='selCA']/div[2]/ul/li[2]").click()
    time.sleep(2)
    browser.find_element_by_id("btnCASave").click()
def sendmail():
    browser.find_element_by_xpath("//ul[@id='menu']/li[5]/a").click()
    time.sleep(2)
    browser.find_element_by_xpath("//table[@id='list']/tbody/tr[1]/td[13]/div/button").click()
    time.sleep(3)
    browser.find_element_by_xpath("//div[@id='SendMethodDialog']/div/div/p/span").click()
    time.sleep(2)
    browser.find_element_by_id("btnSendComfirm").click()
    time.sleep(2)
    print"send mail"
    browser.find_element_by_xpath("//table[@id='list']/tbody/tr[1]/td[2]/div/a").click()
    time.sleep(2)
    browser.find_element_by_xpath("//div[@id='selAffiStatus']/div[1]").click()
    time.sleep(2)
    browser.find_element_by_xpath("//div[@id='selAffiStatus']/div[2]/ul/li[5]").click()
    time.sleep(2)
    browser.find_element_by_id("btnSave").click()
    time.sleep(3)
    te=browser.find_element_by_xpath("//html/body/div[1]/div/div[2]/ul/li/span/a")
    time.sleep(3)
    webdriver.ActionChains(browser).move_to_element(te).perform()
    time.sleep(5)
    browser.find_element_by_xpath("//dl[@id='set_sub_dlid']/dd[4]/a").click()
def pmnewcontact():
    browser.find_element_by_xpath("//div[@class='pm tile double icon bg-color-redCustorm']/div/img").click()  
    time.sleep(2)
    browser.find_element_by_xpath("//ul[@id='menu']/li[3]/a").click()
    time.sleep(2)
    browser.find_element_by_id("btnNew").click()
    time.sleep(2)
    browser.find_element_by_xpath("//body/input").send_keys('d:\\affiliate paperwork\Exhibit D template.xlsx' )
    time.sleep(5)
    browser.find_element_by_id("btnSave").click()
    print "ok go to send the sow contacat"
    time.sleep(2)
    te=browser.find_element_by_xpath("//html/body/div[1]/div/div[2]/ul/li/span/a")
    time.sleep(3)
    webdriver.ActionChains(browser).move_to_element(te).perform()
    time.sleep(2)
    browser.find_element_by_xpath("//dl[@id='set_sub_dlid']/dd[3]/a").click()
def cmpaperwork():
    browser.find_element_by_xpath("//ul[@id='menu']/li[5]/a").click()
    time.sleep(2)
    browser.find_element_by_xpath("//table[@id='list']/tbody/tr[1]/td[13]/div/button").click()
    time.sleep(2)
    browser.find_element_by_xpath("//div[@id='SendMethodDialog']/div/div/p/span").click()
    time.sleep(2)
    browser.find_element_by_id("btnSendComfirm").click()
    time.sleep(2)
    browser.find_element_by_xpath("//table[@id='list']/tbody/tr[1]/td[2]/div/a").click()
    time.sleep(2)
    browser.find_element_by_xpath("//ul[@id='table']/li[2]/span/img").click()
    time.sleep(2)
    browser.find_element_by_xpath("//body/input").send_keys('d:\\affiliate paperwork\ExhibitA.docx' )
    time.sleep(2)
    browser.find_element_by_xpath("//body/input").send_keys('d:\\affiliate paperwork\ExhibitBFacility.docx' )
    time.sleep(2)
    browser.find_element_by_xpath("//body/input").send_keys('d:\\affiliate paperwork\ExhibitA.docx')
    time.sleep(2)
    browser.find_element_by_xpath("//body/input").send_keys('d:\\affiliate paperwork\ExhibitA.docx' )
    time.sleep(2)
      #  browser.find_element_by_xpath("//ul[@id='table']/li[2]/div/div/div[5]/div/tbody/tr/td[7]/div/span").click()
      #  time.sleep(2)
       # browser.find_element_by_xpath("//ul[@id='table']/li[2]/div/div/div[5]/div/tbody/tr[2]/td[7]/div/span").click()
      #  time.sleep(2)
       # browser.find_element_by_xpath("//ul[@id='table']/li[2]/div/div/div[5]/div/tbody/tr[3]/td[7]/div/span").click()
       # time.sleep(2)
      #  browser.find_element_by_xpath("//ul[@id='table']/li[2]/div/div/div[5]/div/tbody/tr[4]/td[7]/div/span").click()
    #time.sleep(2)
    te=browser.find_element_by_xpath("//ul[@id='table']/li[2]/span[6]/div/div/input").text
    print te
    time.sleep(2)
    browser.find_element_by_xpath("//ul[@id='subMenu']/li[4]/a").click()  
    
login('0@cm.com')
time.sleep(2)
cooki=browser.get_cookies()
print "cm login 's %s" %(cooki)
time.sleep(2)
newaffi('slenium test00103')  
time.sleep(2) 
sendmail()
time.sleep(2)
login('4@pc.com')
time.sleep(2) 
pmnewcontact()
time.sleep(2)
login('0@cm.com')
time.sleep(2)
cmpaperwork()
print"work complete"
browser.quit()

























