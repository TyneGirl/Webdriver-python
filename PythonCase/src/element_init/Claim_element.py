#coding=utf-8
'''
Created on 2014��2��24��

@author: ting.liu
'''
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
class Claimlist:
    def claim(self,browser):
        return browser.find_element_by_xpath("//ul[@id='menu']/li[3]/a")
    def ClaimNew(self,browser):
        return browser.find_element_by_id("btnNew")
    def search(self,browser):
        return browser.find_element_by_id("spanSearch")
    def Claimnumber(self,browser):
        return browser.find_element_by_id("s_txtclaim")
    def storenumber(self,browser):
        return browser.find_element_by_id("s_txtstore")
    def claimtype(self,browser):
        return browser.find_element_by_xpath("//div[@id='s_selClaimtype']/div[1]/input[1]")
    def claimIncidentReport(self,browser):
        return browser.find_element_by_xpath("//div[@id='s_selClaimtype']/div[2]/ul/li[2]")
    def ClaimLawsuit(self,browser):
        return browser.find_element_by_xpath("//div[@id='s_selClaimtype']/div[2]/ul/li[3]")
    def PaymentDispute(self,browser):
        return browser.find_element_by_xpath("//div[@id='s_selClaimtype']/div[2]/ul/li[4]")
    def storesaddress(self,browser):
        return browser.find_element_by_id("s_txtstoresaddress")
    def claimadjustername(self,browser):
        return browser.find_element_by_id("s_txtclaimadjustername")
    def ClaimPhone(self,browser):
        return browser.find_element_by_id("s_txtclaimphone")
    def Phone(self,browser):
        return browser.find_element_by_id("s_txtphone")
    def affiliate(self,browser):
        return browser.find_element_by_id("s_txtaffiliate")
    def Customername(self,browser):
        return browser.find_element_by_xpath("//div[@id='s_selsehcustomer']/div[1]/span")
    def customername1(self,browser):
        return browser.find_element_by_xpath("//div[@id='showCustomerName']/ul/li[3]/span[2]")
    def Resolutionstatus(self,browser):
        return browser.find_element_by_xpath("//div[@id='s_selresolutionstatus']/div[1]/input[1]")
    def resolutionOpen(self,browser):
        return browser.find_element_by_xpath("//div[@id='s_selresolutionstatus']/div[2]/ul/li[2]")
    def Claimsearch(self,browser):
        return browser.find_element_by_id("s_search")
    def ClaimCancel(self,browser):
        return browser.find_element_by_id("s_cancel")
    def ClaimTable1(self,browser):
        return browser.find_element_by_xpath("//div[@id='grid']/tbody/tr[1]/td[1]/div")
    
    
    
 
        