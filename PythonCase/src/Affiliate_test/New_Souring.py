#coding=utf-8
'''
Created on 2014��1��13��

@author: ting.liu
'''

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os,time
import random
import math,operator
import Means
import testlog
import traceback
from Data_init import Affiliate_data
from SendEmail import Sendemail,emailimage
from email.mime.text import MIMEText
'''
def highlight(element):
#"""Highlights (blinks) a Selenium Webdriver element"""
    driver = element._parent
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
        element, s)
        original_style = element.get_attribute('style')
        apply_style("background: yellow; border: 2px solid red;")
        time.sleep(.3)
        apply_style(original_style)
'''
test=Affiliate_data.Athlete(['affiliate test','test03','test04','seletest'],'2014-03-06',['215','258','455','987'])

def nessouring():
       
    chromedriver="D:\Program Files (x86)\Chrome\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    browser = webdriver.Chrome(chromedriver) # Get local session of firefox
    browser.maximize_window()
    browser.get("http://192.168.1.20:9999") # Load page
    assert "login" in browser.title
    browser.implicitly_wait(2)
    Means.login(browser, '4@pc.com', '123456') #登录pm
    time.sleep(2)# Let the page load, will be added to the API
    try:
        browser.find_element_by_xpath("//div[@class='pm tile double icon bg-color-redCustorm']/div/img").click()    #using xpath to find element
        time.sleep(2)
        browser.find_element_by_xpath("//ul[@id='menu']/li/a").click()#click sourcing
        time.sleep(1)
        browser.find_element_by_id("btnSearchNew").click()
       # r=random.randint(1,1000)
     #   print r
        browser.find_element_by_id("LegalName").send_keys(test.name[2])
        browser.find_element_by_xpath("//div[@id='entityType']/div").click()
        time.sleep(2)
        entitytype=browser.find_element_by_xpath("//div[@id='entityType']/div[2]/ul/li[3]")
        print "输出entitytype:%s" %(entitytype.text)
        entitytype.click()   #drop list chosen
        time.sleep(2)
        browser.find_element_by_xpath("//div[@id='stateRegistered']/div").click()
        time.sleep(2)
        statere=browser.find_element_by_xpath("//div[@id='stateRegistered']/div[2]/ul/li[7]")
        statere.click()        
        browser.find_element_by_xpath("//input[@id='OfficePhoneAreaCode']").send_keys(test.times[1])
        browser.find_element_by_xpath("//input[@id='OfficePhoneCentralOfficeCode']").send_keys(test.times[2])
        browser.find_element_by_xpath("//input[@id='OfficePhoneStationCode']").send_keys("1881")
        browser.find_element_by_xpath("//input[@id='ContactOfficeAreaCode']").send_keys("545")
        browser.find_element_by_xpath("//input[@id='ContactOfficeCentralOfficeCode']").send_keys(test.times[1])
        browser.find_element_by_xpath("//input[@id='ContactOfficeStationCode']").send_keys("3363")
        
        browser.find_element_by_id("SearchButton").click()
        if test.name[2]=='test01' and entitytype.text=='Corporation' and statere.text=='California(CA)':
            alerts=browser.find_element_by_id("alertSearch")
            print "alert的提示信息是否为：This affiliate already exists in the system ! --- %s" %(alerts.text)
            browser.find_element_by_id("LegalName").send_keys('Simpleok!')
            time.sleep(1)
            browser.find_element_by_id("SearchButton").click()
            time.sleep(1)
        else:
            newbutton=browser.find_element_by_id("NewLeadButton")
            if newbutton.is_displayed():
               print "newbutton显示出来了，直接点击按钮New Lead即可！"
               time.sleep(1)
               browser.find_element_by_id("NewLeadButton").click()
            else:
               print"存在相同的phone #或者是office #,需重新填写phone # 或者Office #,需重新填写；"
               browser.find_element_by_xpath("//input[@id='OfficePhoneAreaCode']").clear()
               time.sleep(1)
               browser.find_element_by_xpath("//input[@id='OfficePhoneAreaCode']").send_keys('829')
               browser.find_element_by_xpath("//input[@id='OfficePhoneCentralOfficeCode']").clear()
               browser.find_element_by_xpath("//input[@id='OfficePhoneCentralOfficeCode']").send_keys("739")
               browser.find_element_by_xpath("//input[@id='OfficePhoneStationCode']").clear()
               browser.find_element_by_xpath("//input[@id='OfficePhoneStationCode']").send_keys("1584")
               browser.find_element_by_xpath("//input[@id='ContactOfficeAreaCode']").clear()
               browser.find_element_by_xpath("//input[@id='ContactOfficeAreaCode']").send_keys("981")
               browser.find_element_by_id("SearchButton").click()
               time.sleep(1)
               browser.find_element_by_id("NewLeadButton").click()
        time.sleep(1)   
        print "检查当前页面的URL:http://192.168.1.20:9999/affiliate/pm/sourcing_detail.html ! ---%s " %(browser.current_url)
        browser.find_element_by_xpath("html/body/form/div[1]/div[1]/button[1]").click()
        save_alert=browser.find_element_by_xpath("html/body/div[1]")
        if save_alert.is_displayed():
            print"save_alert被显示了！显示内容为：Please fill out all mandatory fields!f --- %s "%(save_alert.text)
        else:
            print"save_alert没有显示！！ <此处有BUG>"
        time.sleep(1)
        browser.find_element_by_id("DBAName").send_keys("dba")
        time.sleep(1)
        browser.find_element_by_id("Address_AddressLine1").send_keys("line1")
        browser.find_element_by_id("Address_City").send_keys("city")
        browser.find_element_by_xpath("//div[@id='Address_State']/div").click()
        time.sleep(2)
        browser.find_element_by_xpath("//div[@id='Address_State']/div[2]/ul/li[3]").click()
        browser.find_element_by_id("Address_Zipcode").send_keys("12345")
        browser.find_element_by_id("Address_Country").send_keys("USA")
        browser.find_element_by_id("copyAddress").click()
        time.sleep(1)
        browser.find_element_by_xpath("//div[@id='ContactList']/div/div[2]/ul/li/div/input").send_keys("liui")
        browser.find_element_by_xpath("//div[@id='ContactList']/div/div[2]/ul[2]/li/div/input").send_keys("lting")
        browser.implicitly_wait(2)
        browser.find_element_by_xpath("//div[@id='ContactList']/div/div[2]/ul[2]/li[3]/div/input[2]").send_keys("123")
        browser.find_element_by_xpath("//div[@id='ContactList']/div/div[2]/ul[2]/li[3]/div/input[3]").send_keys("183")
        browser.find_element_by_xpath("//div[@id='ContactList']/div/div[2]/ul[2]/li[3]/div/input[4]").send_keys("1239")
        time.sleep(1)
        browser.find_element_by_id("MBECertified_CheckApplicable").click()
        browser.find_element_by_id("SelfPerformingCrews").send_keys("4")
        browser.find_element_by_id("SubContractedCrews").send_keys("4")
        
        #browser.find_element_by_xpath("//div[@id='ServiceTypes']/div").click
        
        browser.find_element_by_xpath("//ul[@id='Services']/li/div/p/span").click()
        time.sleep(1)
        browser.find_element_by_id("btnAddService").click()
        time.sleep(1)
        services=browser.find_element_by_xpath("//div[@id='ServiceAreas']/div/div/p")
        if services.text=='Repair & Maintenance':
            print"选择的服务类型正确：Repair & Maintenance ---%s" %(services.text)
            browser.find_element_by_xpath("//div[@id='ServiceAreas']/div/div/a").click()
            time.sleep(1)
            browser.find_element_by_xpath("html/body/div[8]/div[3]/div/button[1]").click()
            ServiceArea=browser.find_element_by_id("ServiceTypeError")
            if ServiceArea.text=='At least one service type needs to be selected.':
                print"删除服务范围之后，应有提示语：%s ,显示正确；" %(ServiceArea.text)
            else:
                print"在没有选择任何服务区域的时候，应有提示信息显示：At least one service type needs to be selected.---此处有BUG!"          
        else:
          print "应显示服务类型的名字：Repair & Maintenance---此处有BUG!"  
        browser.find_element_by_xpath("//ul[@id='Services']/li/div/p/span").click()
        time.sleep(1)
        browser.find_element_by_id("btnAddService").click()
        browser.implicitly_wait(2)
        browser.find_element_by_xpath("//div[@id='ServiceAreas']/div[1]/div[2]/div[1]/div[2]/ul/li/input").send_keys("12345")
        browser.find_element_by_xpath("//div[@id='ServiceAreas']/div[1]/div[2]/div[1]/div[2]/ul/li[2]/input").send_keys("12")
        browser.find_element_by_xpath("//div[@id='ServiceAreas']/div[1]/div[2]/div[1]/div[2]/ul/li[3]/input").send_keys("12")
        browser.find_element_by_xpath("//div[@id='ServiceAreas']/div[1]/div[2]/div[1]/div[2]/ul/li[4]/input").send_keys("12")
        
        browser.find_element_by_xpath("//div[@id='ServiceAreas']/div[1]/div[2]/div[1]/div[3]/ul/li[1]/input").send_keys("2")
        browser.find_element_by_xpath("//div[@id='ServiceAreas']/div[1]/div[2]/div[1]/div[3]/ul/li[2]/input").send_keys("1")
        browser.find_element_by_xpath("//div[@id='ServiceAreas']/div[1]/div[2]/div[1]/div[3]/ul/li[3]/input").send_keys("12")
        browser.find_element_by_xpath("//div[@id='ServiceAreas']/div[1]/div[2]/div[1]/div[3]/ul/li[4]/input").send_keys("12")   
        time.sleep(1)
        browser.find_element_by_xpath("//body/form/div[1]/div[6]/button").click()
        time.sleep(1)
        browser.find_element_by_xpath("//body/form/div[1]/div/button[2]").click()
        time.sleep(2)
        browser.find_element_by_xpath("//html/body/div[8]/div[3]/div/button[1]").click()
        #browser.close()
  #  except :
  #      testlog.logsys("运行失败", "控件没找到！")
    except Exception as e:
           print e
           msg = traceback.format_exc()
           testlog.logsys("运行失败", "控件没找到！"+ msg)
           browser.get_screenshot_as_file("D:/svn_QA/Screeshot/NewSourcing.jpg")
       # Sendemail.send_mail(a,'ting Auto test',u'输入特殊字符@#￥￥，返回值应为No Data!---此处有BUG')
           emailimage.AutoSendMail(u"新增sourcing时失败!---此处有BUG,且附件是发送异常时的截图！请参考。"+"\n"+"感谢指导!","D:\\svn_QA\Screeshot\NewSourcing.jpg")
        
#for i in range(10):
  # print i
