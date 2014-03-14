#coding=utf-8
'''
Created on 2014��3��6��

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
from element_init import login_init,Sourcing_init,Pm_affiliateDetail
from SendEmail import Sendemail
from SendEmail import Sendemail,emailimage
from email.mime.text import MIMEText 
def modify_sorcing():
    lo=login_init.loginpage()
    so=Sourcing_init.sourcing()
    det=Pm_affiliateDetail.affiliatedetail()
    chromedriver="D:\Program Files (x86)\Chrome\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    browser = webdriver.Chrome(chromedriver) # Get local session of firefox
    browser.maximize_window()
    browser.get("http://192.168.1.20:9999") # Load page
    assert "login" in browser.title
    browser.implicitly_wait(2)
    Means.login(browser, '4@pc.com', '123456')
    assert "System Integration" in browser.title
    lo.rolechosered(browser).click()
    time.sleep(2)
    so.sour(browser).click()
    time.sleep(1)
    status=so.tabstatus(browser).text
    if status=='Converted':
        print "此sourcing的状态为Converted，其详情页面不能编辑！"
        browser.quit()#不能编辑，退出脚本
    else:
        so.tableone(browser).click()
        le=det.LegalName(browser).text
        #############修改Legal Name字段################
        det.LegalName(browser).clear()
        det.LegalName(browser).send_keys("modifyitsname01")
        name=det.LegalName(browser).text
        det.sosave(browser).click()
        #############确认是否修改成功######################
        if le==name:
            print(le+'更改成了：modifyitsname'+'，此处没有Bug，成功修改！')
            testlog.logsys("此处没有BUG", "---没有BUG")
        else:
            print(le+'没有被修改，此处有BUG，请开发人员修改！---BUG')  #此处要是能做成那种发现bug，自动发送邮件给开发人员就Perfect了！
            browser.get_screenshot_as_file("D:/svn_QA/Screeshot/modifysourname.jpg")
            emailimage.AutoSendMail(u"修改sourcing页面的legal Name---此处有BUG,且附件是发送异常时的截图！请参考。"+"\n"+"感谢指导","D:\\svn_QA\Screeshot\modifysourname.jpg")   
    browser.close()
#modify_sorcing()
    
    