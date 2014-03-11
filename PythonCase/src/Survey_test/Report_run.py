#coding=utf-8

'''
Created on 2014��2��11��

@author: ting.liu
'''
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
class Test(unittest.TestCase):
    def setUp(self):
        chromedriver="D:\Program Files (x86)\Chrome\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.1.20:9999"
        self.verificationErrors = []
    def test_Surveyor(self):
        browser = self.driver
        browser.get(self.base_url)
        browser.maximize_window()
        browser.find_element_by_id("txtAccount").send_keys("tingting008_2013@126.com")
        log=browser.find_element_by_id("txtPwd")
        log.send_keys("123456" + Keys.RETURN)
        WebDriverWait(browser, 5).until(lambda the_driver: browser.find_element_by_link_text("Report").is_displayed())
        browser.find_element_by_link_text("Report").click()
        Uselect=browser.find_element_by_xpath("//select[@id='search_project_id']")
        Uoptions=Uselect.find_elements_by_tag_name("option")
        a=len(Uoptions)
        print a
        browser.find_element_by_xpath("//select[@id='search_project_id']").click()
        time.sleep(1)
        Uselect.find_elements_by_tag_name("option")[3].click()
        time.sleep(1)
        browser.find_element_by_xpath("//a[@id='btnSearch']").click()
        browser.implicitly_wait(2)
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    testsuite=unittest.TestSuite()
#testsuite.addTest(Test("setUp"))
    testsuite.addTest(Test("test_Surveyor"))
#testsuite.addTest(Test("tearDown")) 
    #testsuite.addTest(Test("test_SurveyPM"))
    filename='D:\\result.html'
    fp=file(filename,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(
           stream=fp,
           title='testcase',
           description='test report'
           )
 #   runner=unittest.TextTestRunner()
    runner.run(testsuite)
         
         
        
        
        
        
        