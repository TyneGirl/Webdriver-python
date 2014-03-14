#coding=utf-8
'''
Created on 2014年2月13号

@author: ting.liu
'''
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os,time
from element_init import login_init
#start a application;
def start_firex():
    dr=webdriver.Firefox()
    dr.get("http://192.168.1.20:9999")
def start_chrome():
    chromedriver="D:\Program Files (x86)\Chrome\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    browser = webdriver.Chrome(chromedriver)
    browser.get("http://192.168.1.20:9999")
#start a login;
def login(browser,user,psd):
    lo=login_init.loginpage()
    lo.account(browser).send_keys(user)
    lo.psdaccount(browser).send_keys(psd + Keys.RETURN)
def coverletermsar(browser,name):   #upload the cover paperwork
    #browser.find_element_by_id("btnNew").click()
    time.sleep(2)
    browser.find_element_by_id("templateName").send_keys(name)   #upload the paperwork
    time.sleep(2)
    #browser.find_element_by_id("broseButton").click()
    browser.find_element_by_xpath("//body/input").send_keys('d:\\affiliate paperwork\W9.docx' )
    time.sleep(15)
    browser.find_element_by_id("btnSaveAndNew").click()
    print "done"
def msagern(browser,name):
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
def w9(browser,name):
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
def i9(browser,name):
    browser.find_element_by_xpath("//div[@id='templateType']/div").click()
    time.sleep(2)
    browser.find_element_by_xpath("//div[@id='templateType']/div[2]/ul/li[4]").click()  #click w9
    browser.find_element_by_id("templateName").send_keys(name)
    time.sleep(2)
    browser.find_element_by_xpath("//body/input").send_keys('d:\\affiliate paperwork\I9--Development-ChangSha Office-Compliance Paperwork Templates-MSA-Facitliy-Affiliate MSA - Facilities (2013-05-01) clean (2).docx' )
    time.sleep(15)
    browser.find_element_by_id("btnSaveAndNew").click()
    print "i9okok"
def ExhibitA(browser,name):
    browser.find_element_by_xpath("//div[@id='templateType']/div").click()
    time.sleep(2)
    browser.find_element_by_xpath("//div[@id='templateType']/div[2]/ul/li[5]").click()  #click w9
    browser.find_element_by_id("templateName").send_keys(name)
    time.sleep(2)
    browser.find_element_by_xpath("//body/input").send_keys('d:\\affiliate paperwork\ExhibitA.docx')
    time.sleep(10)
    browser.find_element_by_id("btnSaveAndNew").click()
    print "exhibitAokok"
def ExhibitB(browser,name):
    browser.find_element_by_xpath("//div[@id='templateType']/div").click()
    time.sleep(2)
    browser.find_element_by_xpath("//div[@id='templateType']/div[2]/ul/li[6]").click()  #click w9
    browser.find_element_by_id("templateName").send_keys(name)
    time.sleep(2)
    browser.find_element_by_xpath("//body/input").send_keys('d:\\affiliate paperwork\ExhibitBFacility.docx')
    time.sleep(10)
    browser.find_element_by_id("btnSaveAndNew").click()
    print "exhibitBokok"
def ExhibitD(browser,name):
    browser.find_element_by_xpath("//div[@id='templateType']/div").click()
    time.sleep(2)
    browser.find_element_by_xpath("//div[@id='templateType']/div[2]/ul/li[7]").click()  #click w9
    browser.find_element_by_id("templateName").send_keys(name)
    time.sleep(2)
    browser.find_element_by_xpath("//body/input").send_keys('d:\\affiliate paperwork\Exhibit D template.xlsx')
    time.sleep(10)
    browser.find_element_by_id("btnSaveAndNew").click()
    print "exhibitBokok"
def ExhibitDAmendment(browser,name):
    browser.find_element_by_xpath("//div[@id='templateType']/div").click()
    time.sleep(1)
    browser.find_element_by_xpath("//div[@id='templateType']/div[2]/ul/li[8]").click()
    browser.find_element_by_id("templateName").send_keys(name)
    browser.find_element_by_xpath("//body/input").send_keys('d:\\affiliate paperwork\Exhibit D Amendment Family Dollar Floor Care Store List with Pricing- Template - EchoSign (9.18.13)(1) (1).xlsx' )
    time.sleep(10)
    browser.find_element_by_id("btnSaveAndNew").click()
