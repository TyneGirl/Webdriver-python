#-*-coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
class login(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Firefox()

        self.driver.implicitly_wait(30)

        self.base_url = "http://www.51testing.com/"

        self.verificationErrors = []
    def test_51login(self):

        driver = self.driver

        driver.get(self.base_url + "/html/index.html")

        driver.find_element_by_id("username").send_keys("dj7491916")

        driver.find_element_by_id("userpass").send_keys("y0031936")

        driver.find_element_by_id("dologin").click()

        verify=raw_input("please enter vertify number:")

        driver.find_element_by_id("xspace-seccode").send_keys(verify)

        driver.find_element_by_id("securitysubmit").click()


        firstelement=driver.find_element_by_class_name("xboxcontent")

        el=firstelement.find_elements_by_tag_name("a")

        for i in el:

            print i.text

    def tearDown(self):

        self.driver.quit()

        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":

    unittest.main()