#coding=utf-8
'''
Created on 2014��2��24��

@author: ting.liu
'''
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
class MyClass(object):
    def Claimdetailnumber(self,browser):
        return browser.find_element_by_id("txtCClaimNo")
    #email address
    def emailaddress(self,browser):
        return browser.find_element_by_id("txtCEmailAddress")
    def alternativnumber(self,browser):
        return browser.find_element_by_id("txtCAlternativeNumberOne")
    def alternativenumber2(self,browser):
        return browser.find_element_by_id("txtCAlternativeNumberTwo")
    def alternativenumber3(self,browser):
        return browser.find_element_by_id("txtCAlternativeNumberThree")    
    def alternativenumber4(self,browser):
        return browser.find_element_by_id("txtCAlternativeNumberFour")
    def Claimaffiliate(self,browser):
        return browser.find_element_by_xpath("//div[@id='selCAffiliate']/div[1]/span")
    def Claimaffiliate1(self,browser):
        return browser.find_element_by_xpath("//div[@id='showCustomerName']/ul/li[2]")
    def Claimaffiliate2(self,browser):
        return browser.find_element_by_xpath("//div[@id='showCustomerName']/ul/li[3]/span[2]")
    def Customername(self,browser):
        return browser.find_element_by_xpath("//div[@id='selCCustomerClient']/div[1]/span")
    def Customername2(self,browser):
        return browser.find_element_by_xpath("//div[@id='showCustomerName']/ul/li[3]/span[2]")
    def ContractName(self,browser):
        return browser.find_element_by_xpath("//div[@id='selCContractName']/div[1]/span")
    def AddService(self,browser):
        return browser.find_element_by_id("btnCAddService")
    def AdServiceType(self,browser):
        return browser.find_element_by_id("txtCAddService_ServiceType")
    def AdServiceDate(self,browser):
        return browser.find_element_by_id("txtCAddService_ServiceDate")
    def AdServiceDate1(self,browser):
        return browser.find_element_by_xpath("//div[@id='ui-datepicker-div']/table/tbody/tr[5]/td[4]/a")
    #add service 里面的add notes
    def AdNote(self,browser):
        return browser.find_element_by_id("txtCAddService_Notes")
    #add service中的User字段
    def AdUser(self,browser):
        return browser.find_element_by_id("txtCAddService_User")
    #add service中的Add按钮
    def AdServiceAdd(self,browser):
        return browser.find_element_by_id("btnCAddService_Add")
    #add service中的Cancel按钮
    def AdServiceCancel(self,browser):
        return browser.find_element_by_id("btnCAddService_Cancel")
    #Claim detail页面中的Claim Type
    def ClaimType(self,browser):
        return browser.find_element_by_xpath("//div[@id='selCClaimType']/div[1]/input[1]")
    def ClaimType2(self,browser):
        return browser.find_element_by_xpath("//div[@id='selCClaimType']/div[2]/ul/li[2]")
    
    #set by字段
    def ClaimSetby(self,browser):
        return browser.find_element_by_id("txtCSetBy")
    #store's address字段
    def Claimstoreaddreess(self,browser):
        return browser.find_element_by_id("txtCStoryAddress")
    #claim phone number
    def Claimphonenumber(self,browser):
        return browser.find_element_by_id("txtCClaimPhoneNumberOne")
    def Claimphonenumber2(self,browser):
        return browser.find_element_by_id("txtCClaimPhoneNumberTwo")
    def Claimphonenumber3(self,browser):
        return browser.find_element_by_id("txtCClaimPhoneNumberThree")
    def Claimphonenumber4(self,browser):
        return browser.find_element_by_id("txtCClaimPhoneNumberFour")
    #Claim Synopsis
    def Claimsynopsis(self,browser):
        return browser.find_element_by_id("txtCClaimSynopsis")
    #injury type字段
    def injurytype(self,browser):
        return browser.find_element_by_xpath("//div[@id='selCInjuryType']/div[1]/input[1]")
    def injurytype2(self,browser):
        return browser.find_element_by_xpath("//div[@id='selCInjuryType']/div[2]/ul/li[2]")
    def injurytype3(self,browser):
        return browser.find_element_by_xpath("//div[@id='selCInjuryType']/div[2]/ul/li[3]")
    #statutory limit
    def statutorylimit(self,browser):
        return browser.find_element_by_xpath("//div[@id='selCStatutoryLimit']/div[1]/input[1]")
    # statutory limit 1year
    
    def statutorylimit1(self,browser):
        return browser.find_element_by_xpath("//div[@id='selCStatutoryLimit']/div[2]/ul/li[2]")
    #store number
    def storenumber(self,browser):
        return browser.find_element_by_id("txtCStoryNumber")
    #Claimant
    def Claimant(self,browser):
        return browser.find_element_by_id("txtCClaimant")
    #Claim Address
    def Claimaddress(self,browser):
        return browser.find_element_by_id("txtCClaimAddress")
    #点击
    
        
    
    
    
    
    
    
    
    
    
    
    
