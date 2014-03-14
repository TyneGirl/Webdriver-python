#coding=utf-8
'''
Created on 2014��3��11��

@author: ting.liu
'''
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os,time
from element_init import Pm_affiliate_search
from element_init import login_init,Sourcing_init
import Means
from SendEmail import Sendemail,emailimage
from email.mime.text import MIMEText


def sourcing_search():
    a=['19066367@qq.com','1152037739@qq.com','loveholly519@qq.com']
    lo=login_init.loginpage()
    so=Sourcing_init.sourcing()
    Un=Pm_affiliate_search.affiliatesearch()
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
    Un.affiliateSearchfunction(browser).click()
    Un.Searchaffiliatename(browser).send_keys("@#$^&*^")
    time.sleep(1)
    Un.searchbutton(browser).click()
    ndata=Un.shownodata(browser).text
    if ndata=="No Data01":
        print "输入特殊字符@￥@￥￥，返回值为No Data,此处没有BUG"
    else:
        print"输入特殊字符@#￥￥，返回值应为No Data!---此处有BUG"
        browser.get_screenshot_as_file("D:/svn_QA/Screeshot/sourcingsearch.jpg")
       # Sendemail.send_mail(a,'ting Auto test',u'输入特殊字符@#￥￥，返回值应为No Data!---此处有BUG')
        emailimage.AutoSendMail(u"输入特殊字符@#￥￥，返回值应为No Data!---此处有BUG,且附件是发送异常时的截图！请参考。"+"\n"+"感谢指导","D:\\svn_QA\Screeshot\sourcingsearch.jpg")
    browser.close()
#sourcing_search()
        

    
    