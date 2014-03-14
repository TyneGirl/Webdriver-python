#coding=utf-8
'''
Created on 2014��2��21��

@author: ting.liu
'''
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os,time
class sourcing():
    def sour(self,browser):
        return browser.find_element_by_xpath("//ul[@id='menu']/li[1]/a")
    #click the create new lead button
    def newlead(self,browser):
        return browser.find_element_by_id("btnSearchNew")
    #click the callback lead
    def callback(self,browser):
        return browser.find_element_by_id("a_callbackAffi")
    #click the Leads from Website
    def leadwebsite(self,browser):
        return browser.find_element_by_id("btnviewLead")
    #click the table
    def tableone(self,browser):
        return browser.find_element_by_xpath("//div[@id='grid']/tbody/tr[1]/td[2]")
    def tabstatus(self,browser):
        return browser.find_element_by_xpath("//div[@id='grid']/tbody/tr[1]/td[9]/div")
    def detailstat(self,browser):
        return browser.find_element_by_id("Status")
    
    
        