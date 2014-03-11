from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import os,time
import unittest
import HTMLTestRunner
import unittest 
import sys 
import StringIO 
class Testlist(unittest.TestCase): 
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.1.20:9999"
        self.verificationErrors = []
    def test_login(self): 
        browser = self.driver
        browser.maximize_window()
        browser.get(self.base_url + "/account/login.html" )
        time.sleep(2)
        browser.find_element_by_id("txtAccount").send_keys("tingting008_2013@126.com")
        log=browser.find_element_by_id("txtPwd")
        log.send_keys("123456" + Keys.RETURN)
        time.sleep(2)
        print "test1" 
    def test_link(self):
        browser = self.driver
        browser.find_element_by_xpath("//div[@id='content']/div/div[3]/dl/dd[4]/a").click()
        browser.find_element_by_xpath("//div[@id='PhotoGalleryWrap']/div[2]/div/dl/dt/a/img").click()
        
        print "test2"    
def suiting(): 
    filename ="d:\\result.html" 
    fp = file(filename,"wb") 
    suit = unittest.TestSuite() 
    suit.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(Testlist)) 
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="testing result",description="trying") 
    runner.run(suit) 
suiting() 

