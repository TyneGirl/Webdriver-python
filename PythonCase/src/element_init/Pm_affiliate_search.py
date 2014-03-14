#coding=utf-8
'''
Created on 2014��2��20��

@author: ting.liu
'''
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import os,time
class affiliatesearch:
    def affiliatesearchlist(self,browser):
        return browser.find_element_by_xpath("//ul[@id='menu']/li[2]/a")
    def affiliateNew(self,browser):
        return browser.find_element_by_id("btnNewAffiliate")
    def affiliatesearchmapview(self,browser):
        return browser.find_element_by_xpath("//button[@id='btnLinkMap']")
    def affiliatetablelist(self,browser):
        return browser.find_element_by_xpath("//table[@id='grid']/tbody/tr[1]/td[2]/div")
    def affiliateSearchfunction(self,browser):
        return browser.find_element_by_id("propertySearch")
    def Searchaffiliatename(self,browser):
        return browser.find_element_by_id("legalName")
    def searchentity(self,browser):
        return browser.find_element_by_xpath("//div[@id='entityType']/div[1]/input[1]")
    def entitychildrenLLC(self,browser):
        return browser.find_element_by_xpath("//div[@id='entityType']/div[2]/ul/li[2]")
    def entitychildrenLLP(self,browser):
        return browser.find_element_by_xpath("//div[@id='entityType']/div[2]/ul/li[3]")
    def entitychildrenCorporation(self,browser):
        return browser.find_element_by_xpath("//div[@id='entityType']/div[2]/ul/li[4]")
    def entitychildrenSorp(self,browser):
        return browser.find_element_by_xpath("//div[@id='entityType']/div[2]/ul/li[5]")
    def Phone(self,browser):
        return browser.find_element_by_id("phone")
    def affiliatecode(self,browser):
        return browser.find_element_by_id("affiliateCode")
    def city(self,browser):
        return browser.find_element_by_id("city")    
    def CAselect(self,browser):
        return browser.find_element_by_xpath("//div[@id='ca']/div[1]/input[1]")
    def CAselect02(self,browser):
        return browser.find_element_by_xpath("//div[@id='ca']/div[2]/ul/li[2]")
    def CAselect03(self,browser):
        return browser.find_element_by_xpath("//div[@id='ca']/div[2]/ul/li[3]")
    def CAselect04(self,browser):
        return browser.find_element_by_xpath("//div[@id='ca']/div[2]/ul/li[4]")
    def State(self,browser):
        return browser.find_element_by_xpath("//div[@id='state']/div[1]/input[1]")
    def statena(self,browser):
        return browser.find_element_by_xpath("//div[@id='state']/div[2]/ul/li[2]")
    def stateAl(self,browser):
        return browser.find_element_by_xpath("//div[@id='state']/div[2]/ul/li[3]")
    def stateAk(self,browser):
        return browser.find_element_by_xpath("//div[@id='state']/div[2]/ul/li[4]")
    def statAs(self,browser):
        return browser.find_element_by_xpath("//div[@id='state']/div[2]/ul/li[5]")
    def zip(self,browser):
        return browser.find_element_by_id("zip")
    def searchbutton(self,browser):
        return browser.find_element_by_id("btnSearch")
    def searchbuttoncancel(self,browser):
        return browser.find_element_by_id("btnCancel")
    def shownodata(self,browser):
        return browser.find_element_by_id("pager")
    
    
    
    
        
        