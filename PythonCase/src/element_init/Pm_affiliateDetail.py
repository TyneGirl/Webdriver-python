#coding=utf-8
'''
Created on 2014��2��21��

@author: ting.liu
'''
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
class affiliatedetail:
    def affiiatedetail(self,browser):
        return browser.find_element_by_xpath("//ul[@id='subMenu']/li[1]/a")
    def Managers(self,browser):
        return browser.find_element_by_xpath("//ul[@id='subMenu']/li[2]/a")
    def Compliance(self,browser):
        return browser.find_element_by_xpath("//ul[@id='subMenu']/li[3]/a")
    def Document(self,browser):
        return browser.find_element_by_xpath("//ul[@id='subMenu']/li[4]/a")
    def Save(self,browser):
        return browser.find_element_by_xpath("html/body/div[3]/div[1]/form/div[1]/button[1]")
    def sosave(self,browser):
        return browser.find_element_by_xpath('html/body/form/div[1]/div[1]/button[1]')
    def Cancel(self,browser):
        return browser.find_element_by_xpath("html/body/div[3]/div[1]/form/div[1]/button[2]")
    def DBAname(self,browser):
        return browser.find_element_by_id("DBAName")
    def LegalName(self,browser):
        return browser.find_element_by_id("Name")
    def EntityType(self,browser):
        return browser.find_element_by_xpath("//div[@id='EntityType']/div[1]/input[1]")
    def EntityTypeLLC(self,browser):
        return browser.find_element_by_xpath("//div[@id='EntityType']/div[2]/ul/li[1]")
    def EntityTypeLLP(self,browser):
        return browser.find_element_by_xpath("//div[@id='EntityType']/div[2]/ul/li[2]")
    def EntityTypeCorporation(self,browser):
        return browser.find_element_by_xpath("//div[@id='EntityType']/div[2]/ul/li[3]")
    def EntityTypeSolePro(self,browser):
        return browser.find_element_by_xpath("//div[@id='EntityType']/div[2]/ul/li[4]")
    def OtherName(self,browser):
        return browser.find_element_by_id("OtherName")
    def PayableName(self,browser):
        return browser.find_element_by_id("PayableName")
    def OfficePhone1(self,browser):
        return browser.find_element_by_id("Phone_1")
    def OfficePhone2(self,browser):
        return browser.find_element_by_id("Phone_2")
    def OfficePhone3(self,browser):
        return browser.find_element_by_id("Phone_3")
    def OfficePhone4(self,browser):
        return browser.find_element_by_id("Phone_4")
    def StateRegistered(self,browser):
        return browser.find_element_by_xpath("//div[@id='StateRegistered']/div[1]/input[1]")
    def StateRegisteredAL(self,browser):
        return browser.find_element_by_xpath("//div[@id='StateRegistered']/div[2]/ul/li[2]")
    def StateRegisteredAK(self,browser):
        return browser.find_element_by_xpath("//div[@id='StateRegistered']/div[2]/ul/li[3]")
    def StateRegisteredAS(self,browser):
        return browser.find_element_by_xpath("//div[@id='StateRegistered']/div[2]/ul/li[4]")
    def StateRegisteredAZ(self,browser):
        return browser.find_element_by_xpath("//div[@id='StateRegistered']/div[2]/ul/li[4]")
    def Fax1(self,browser):
        return browser.find_element_by_id("Fax_1")
    def Fax2(self,browser):
        return browser.find_element_by_id("Fax_2")
    def Fax3(self,browser):
        return browser.find_element_by_id("Fax_3")   
    def CompanyWebsite(self,browser):
        return browser.find_element_by_id("Website")
    #Address
    def AddressLine1(self,browser):
        return browser.find_element_by_id("Address_AddressLine1")
    def AddressLine1Small(self,browser):
        return browser.find_element_by_xpath("//div[@id='affiliate_profile']/div[3]/ul[1]/li[1]/div/small")
    def AddressLine2(self,browser):
        return browser.find_element_by_id("Address_AddressLine2")
    def City(self,browser):
        return browser.find_element_by_id("Address_City")
    def State(self,browser):
        return browser.find_element_by_xpath("//div[@id='Address_State']/div[1]/input[1]")
    def StateAL(self,browser):
        return browser.find_element_by_xpath("//div[@id='Address_State']/div[2]/ul/li[1]")
    def StateAK(self,browser):
        return browser.find_element_by_xpath("//div[@id='Address_State']/div[2]/ul/li[2]")
    def StateAS(self,browser):
        return browser.find_element_by_xpath("//div[@id='Address_State']/div[2]/ul/li[3]")
    def Zip(self,browser):
        return browser.find_element_by_id("Address_Zipcode")
    def Country(self,browser):
        return browser.find_element_by_id("Address_Country")
    def SameasBusinessAddress(self,browser):
        return browser.find_element_by_id("copyAddress")
    #MBE
    def MBEcheck(self,browser):
        return browser.find_element_by_id("MBECertified_CheckApplicable")
    def MBEcertificate(self,browser):
        return browser.find_element_by_id("MBECertified_IsProve")
    def MBEdocument(self,browser):
        return browser.find_element_by_xpath("//div[@id='MBECertified_Document_div']/div")
    #WBE
    def WBEcheck(self,browser):
        return browser.find_element_by_id("WBECertified_CheckApplicable")
    def WBEcertificate(self,browser):
        return browser.find_element_by_id("WBECertified_IsProve")
    def WBEdocument(self,browser):
        return browser.find_element_by_xpath("//div[@id='WBECertified_Document_div']/div")
    #DBE
    def DBEcheck(self,browser):
        return browser.find_element_by_id("DBECertified_CheckApplicable")
    def DBEcertificate(self,browser):
        return browser.find_element_by_id("DBECertified_IsProve")
    def DBEdocument(self,browser):
        return browser.find_element_by_xpath("//div[@id='DBECertified_Document_div']/div") 
    #none of the above
    def Noneoftheabove(self,browser):
        return browser.find_element_by_id("OtherCertified")
    #Crews
    def selfPerformingCrews(self,browser):
        return browser.find_element_by_id("SelfPerformingCrews")
    def subContractedCrew(self,browser):
        return browser.find_element_by_id("SubContractedCrews")
    #communication checkbox
    def communicate(self,browser):
        return browser.find_element_by_id("Communications_Email")
    def communicate1(self,browser):
        return browser.find_element_by_id("Communications_Fax")
    def communicate3(self,browser):
        return browser.find_element_by_id("Communications_PDF")
    #Payment Terms dropdown
    def paymentterms(self,browser):
        return browser.find_element_by_xpath("//div[@id='PaymentTerms']/div[1]/input[1]")    
    def payment60days(self,browser):
        return browser.find_element_by_xpath("//div[@id='PaymentTerms']/div[2]/ul/li[1]")
    def payment45days(self,browser):
        return browser.find_element_by_xpath("//div[@id='PaymentTerms']/div[2]/ul/li[2]")
    def payment30days(self,browser):
        return browser.find_element_by_xpath("//div[@id='PaymentTerms']/div[2]/ul/li[3]")
    def payment15days(self,browser):
        return browser.find_element_by_xpath("//div[@id='PaymentTerms']/div[2]/ul/li[4]")
    def payment015days(self,browser):
        return browser.find_element_by_xpath("//div[@id='PaymentTerms']/div[2]/ul/li[5]")
    def paymentweekly(self,browser):
        return browser.find_element_by_xpath("//div[@id='PaymentTerms']/div[2]/ul/li[6]")
    #affiliate customer
    def customer(self,browser):
        return browser.find_element_by_id("AffiliateCustomer")
    #Note
    def note(self,browser):
        return browser.find_element_by_id("Notes")
    #Contact
    def firstname(self,browser):
        return browser.find_element_by_xpath("//div[@id='ContactList']/div/div[2]/ul/li/div/input")
    def lastname(self,browser):
        return browser.find_element_by_xpath("//div[@id='ContactList']/div/div[2]/ul[2]/li/div/input")
    def office1(self,browser):
        return browser.find_element_by_xpath("//div[@id='ContactList']/div/div[2]/ul[2]/li[2]/div/input[2]")
    def office2(self,browser):
        return browser.find_element_by_xpath("//div[@id='ContactList']/div/div[2]/ul[2]/li[2]/div/input[3]")
    def office3(self,browser):
        return browser.find_element_by_xpath("//div[@id='ContactList']/div/div[2]/ul[2]/li[2]/div/input[4]")
    def office4(self,browser):
        return browser.find_element_by_xpath("//div[@id='ContactList']/div/div[2]/ul[2]/li[2]/div/input[5]")
    
    #email
    def email(self,browser):
        return browser.find_element_by_xpath("//div[@id='ContactList']/div/div[2]/ul/li[5]/div/div/div/input")
    def emailyes(self,browser):
        return browser.find_element_by_xpath("//div[@id='ContactList']/div/div[2]/ul/li[5]/div/div/div[2]/ul/li")
    
    #service
    
    def survicetype(self,browser):
        return browser.find_element_by_xpath("//div[@id='ServiceTypes']/div[1]/input[1]")
    #Repair & Maintenance
    def RepairMani(self,browser):
        return browser.find_element_by_xpath("//div[@id='ServiceTypes']/div[2]/ul/li[1]")
    # repair & Maintenance Refrigeration
    def Refrigeration(self,browser):
        return browser.find_element_by_xpath("//ul[id='Services']/li/div/p/span")
    #add to the service area button
    def addtoservice(self,browser):
        return browser.find_element_by_xpath("//div[@id='btnAddService']/a")
    # Service Area zhong de title
    def serviceareatitle(self,browser):
        return browser.find_element_by_xpath("//div[@id='ServiceAreas']/div/div/p")
    #service area zhogn de zip code
    def serviceareazip(self,browser):
        return browser.find_element_by_xpath("//div[@id='ServiceAreas']/div/div[2]/div/div[2]/ul/li/div/input")
    #Mile Radius
    def servicearearadius(self,browser):
        return browser.find_element_by_xpath("//div[@id='ServiceAreas']/div/div[2]/div/div[3]/ul/li/div/input")
    #Regular Rate
    def regularrate(self,browser):
        return browser.find_element_by_xpath("//div[@id='ServiceAreas']/div/div[2]/div/div[2]/ul/li[2]/div/input")
    #Overtime Rate
    def overtimerate(self,browser):
        return browser.find_element_by_xpath("//div[@id='ServiceAreas']/div/div[2]/div/div[3]/ul/li[2]/div/input")
    #Holiday Rate
    def holidayrate(self,browser):
        return browser.find_element_by_xpath("//div[@id='ServiceAreas']/div/div[2]/div/div[2]/ul/li[3]/div/input")
    #Trip Rates
    def Triprate(self,browser):
        return browser.find_element_by_xpath("//div[@id='ServiceAreas']/div/div[2]/div/div[3]/ul/li[3]/div/input")
    #serivece Fee
    def ServiceFree(self,browser):
        return browser.find_element_by_xpath("//div[@id='ServiceAreas']/div/div[2]/div/div[2]/ul/li[4]/div/input")
    #Material Markup%
    def materialmarkup(self,browser):
        return browser.find_element_by_xpath("//div[@id='ServiceAreas']/div/div[2]/div/div[3]/ul/li[4]/div/input")
    
    
    
    
    
    
    
    
     
    
    
    
     

        