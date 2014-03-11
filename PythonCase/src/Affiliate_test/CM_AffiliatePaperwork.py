#coding=utf-8
'''
Created on 2014��1��13��

@author: ting.liu
'''
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os,time
chromedriver="D:\Program Files (x86)\Chrome\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)
browser.maximize_window()
browser.get("http://192.168.1.20:9999") # Load page
def login():
    browser.find_element_by_id("txtAccount").send_keys("0@cm.com")
    log=browser.find_element_by_id("txtPwd")
    log.send_keys("123456" + Keys.RETURN)
login()    #login the cm
time.sleep(2)
te=browser.find_element_by_xpath("//ul[@id='menu']/li[6]/a/span")
#browser.find_element_by_xpath("//ul[@id='menu']/li[6]/a/span").click()
time.sleep(3)
#menu = te.find_element_by_link_text('Paperwork Templates')
webdriver.ActionChains(browser).move_to_element(te).perform()
time.sleep(2)
browser.find_element_by_xpath("//ul[@id='menu']/li[6]/ul/li[2]/a").click()
time.sleep(2)
browser.find_element_by_id("btnNew").click()
def coverletermsar(name):   #upload the cover paperwork
    #browser.find_element_by_id("btnNew").click()
    time.sleep(2)
    browser.find_element_by_id("templateName").send_keys(name)   #upload the paperwork
    time.sleep(2)
    #browser.find_element_by_id("broseButton").click()
    browser.find_element_by_xpath("//body/input").send_keys('d:\\affiliate paperwork\W9.docx' )
    time.sleep(15)
    browser.find_element_by_id("btnSaveAndNew").click()
    print "done"
def msagern(name):
    browser.find_element_by_xpath("//div[@id='templateType']/div").click()
    time.sleep(2)
    browser.find_element_by_xpath("//div[@id='templateType']/div[2]/ul/li[2]").click()  #click msa
    browser.find_element_by_id("templateName").send_keys(name)
    time.sleep(2)
    browser.find_element_by_xpath("//body/input").send_keys('d:\\affiliate paperwork\MSAgeneral.docx' )
    print "msa gneral"
    time.sleep(15)
    browser.find_element_by_id("btnSaveAndNew").click()
    print "good"
def w9(name):
    browser.find_element_by_xpath("//div[@id='templateType']/div").click()
    time.sleep(2)
    browser.find_element_by_xpath("//div[@id='templateType']/div[2]/ul/li[3]").click()  #click w9
    time.sleep(2)
    browser.find_element_by_id("templateName").send_keys(name)
    time.sleep(2)
    browser.find_element_by_xpath("//body/input").send_keys('d:\\affiliate paperwork\W9.docx' )
    time.sleep(10)
    browser.find_element_by_id("btnSaveAndNew").click()
    print"msaok"
def i9(name):
    browser.find_element_by_xpath("//div[@id='templateType']/div").click()
    time.sleep(2)
    browser.find_element_by_xpath("//div[@id='templateType']/div[2]/ul/li[4]").click()  #click w9
    browser.find_element_by_id("templateName").send_keys(name)
    time.sleep(2)
    browser.find_element_by_xpath("//body/input").send_keys('d:\\affiliate paperwork\I9--Development-ChangSha Office-Compliance Paperwork Templates-MSA-Facitliy-Affiliate MSA - Facilities (2013-05-01) clean (2).docx' )
    time.sleep(15)
    browser.find_element_by_id("btnSaveAndNew").click()
    print "i9okok"
def ExhibitA(name):
    browser.find_element_by_xpath("//div[@id='templateType']/div").click()
    time.sleep(2)
    browser.find_element_by_xpath("//div[@id='templateType']/div[2]/ul/li[5]").click()  #click w9
    browser.find_element_by_id("templateName").send_keys(name)
    time.sleep(2)
    browser.find_element_by_xpath("//body/input").send_keys('d:\\affiliate paperwork\ExhibitA.docx')
    time.sleep(10)
    browser.find_element_by_id("btnSaveAndNew").click()
    print "exhibitAokok"
def ExhibitB(name):
    browser.find_element_by_xpath("//div[@id='templateType']/div").click()
    time.sleep(2)
    browser.find_element_by_xpath("//div[@id='templateType']/div[2]/ul/li[6]").click()  #click w9
    browser.find_element_by_id("templateName").send_keys(name)
    time.sleep(2)
    browser.find_element_by_xpath("//body/input").send_keys('d:\\affiliate paperwork\ExhibitBFacility.docx')
    time.sleep(10)
    browser.find_element_by_id("btnSaveAndNew").click()
    print "exhibitBokok"
def ExhibitD(name):
    browser.find_element_by_xpath("//div[@id='templateType']/div").click()
    time.sleep(2)
    browser.find_element_by_xpath("//div[@id='templateType']/div[2]/ul/li[7]").click()  #click w9
    browser.find_element_by_id("templateName").send_keys(name)
    time.sleep(2)
    browser.find_element_by_xpath("//body/input").send_keys('d:\\affiliate paperwork\Exhibit D template.xlsx')
    time.sleep(10)
    browser.find_element_by_id("btnSaveAndNew").click()
    print "exhibitBokok"
def ExhibitDAmendment(name):
    browser.find_element_by_xpath("//div[@id='templateType']/div").click()
    time.sleep(1)
    browser.find_element_by_xpath("//div[@id='templateType']/div[2]/ul/li[8]").click()
    browser.find_element_by_id("templateName").send_keys(name)
    browser.find_element_by_xpath("//body/input").send_keys('d:\\affiliate paperwork\Exhibit D Amendment Family Dollar Floor Care Store List with Pricing- Template - EchoSign (9.18.13)(1) (1).xlsx' )
    time.sleep(10)
    browser.find_element_by_id("btnSaveAndNew").click()
time.sleep(3)
coverletermsar('seleniumparametest01034')
time.sleep(2)
msagern('seleniumtestmsa014')
time.sleep(2)
w9('seleniumtestW9014')
time.sleep(2)
i9('seleniumtestI9014')
time.sleep(2)
ExhibitA('seleniumtestExhibitA014')
time.sleep(2)
ExhibitB('seleniumtestExhibitB014')
time.sleep(2)
ExhibitD('seleniumtestExhibitD014')
time.sleep(2)
ExhibitDAmendment('seleniumtestExhibitdAmendement4')
time.sleep(2)
print"good test"
browser.quit()








