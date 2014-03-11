#coding=utf-8
'''
Created on 2014��3��6��

@author: ting.liu
'''

class Athlete:
    def __init__(self,a_name=[],a_dob=None,phone=[]):
        self.name=a_name
        self.dob=a_dob
        self.times=phone
    def add_name(self,name_value):
        self.name.append(name_value)
    def add_names(self,name_list):
        self.name.extend(name_list)
        
