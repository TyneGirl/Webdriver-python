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
import unittest
import logging
class Test(unittest.TestCase):
   def setUp(self):
        chromedriver="D:\Program Files (x86)\Chrome\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver        
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.1.20:9999"
        self.verificationErrors = []
   def test_SurveyPM(self):
        driver = self.driver
        driver.get(self.base_url + "/account/login.html" )
        time.sleep(2)
        driver.find_element_by_id("txtAccount").send_keys("4@pc.com")
        log=driver.find_element_by_id("txtPwd")
        log.send_keys("123456" + Keys.RETURN)
        time.sleep(2)
        try:
             driver.find_element_by_xpath("//div[@class='pm tile double icon bg-color-blueLight']/div/img").click()   
             driver.find_element_by_xpath("//div[@id='content']/div[1]/div/div[7]/div[1]/a").click()
             time.sleep(2)
             driver.find_element_by_xpath("//html/body/div[2]/div[2]/ul/li[1]/a").click()
             time.sleep(2)
             driver.find_element_by_xpath("//html/body/div[2]/div[2]/ul/li[2]/a").click()
             time.sleep(2)
             driver.find_element_by_xpath("html/body/div[2]/div[2]/ul/li[3]/a").click()
             time.sleep(2)
             driver.find_element_by_xpath("html/body/div[2]/div[2]/ul/li[4]/a").click()
             time.sleep(2)
             driver.find_element_by_id("tasksLink").click()
             time.sleep(2)
             driver.find_element_by_id("locationLink").click()
             time.sleep(2)
             driver.find_element_by_id("surveyorCompanyLink").click()
             time.sleep(2)
             driver.find_element_by_xpath("html/body/div[1]/div/div[1]/a[2]").click()
             time.sleep(2)
             driver.find_element_by_xpath("html/body/div[1]/div/div[1]/a[3]").click()
             time.sleep(2)
             driver.find_element_by_xpath("html/body/div[1]/div/div[1]/a[4]").click()
             logging.basicConfig(filename = os.path.join(os.getcwd(), 'log.txt'), level = logging.DEBUG)  
             logging.debug('this is a message')   
#             os.system('E:\eclipse\PythonCase\src\Python27/ Share_test.py >>log.txt ')   
        except:
             print"ok"
             driver.get_screenshot_as_file("D:/screenshots/test01.png")
             time.sleep(5)
            
   def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
      
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()