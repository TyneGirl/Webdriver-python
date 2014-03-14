#coding:utf-8
'''
Created on 2014年2月20号

@author: ting.liu
'''
import logging
# create logger
module_logger = logging.getLogger("spam_application.auxiliary")
class Auxiliary:
    def __init__(self):
        self.logger = logging.getLogger("spam_application.auxiliary.Auxiliary")
        self.logger.info("creating an instance of Auxiliary")
    def do_something(self):
        self.logger.info("doing something01")
        a = 1 + 1
        self.logger.info("done doing something02")
def some_function():
    module_logger.info("done  ")
