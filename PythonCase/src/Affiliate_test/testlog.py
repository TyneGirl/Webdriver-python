#coding=utf-8
'''
Created on 2014��2��20��

@author: ting.liu
'''
import logging
import auxiliary_module
# create logger with "spam_application"
def logsys(erroinfo,successinfo):
    logger = logging.getLogger("resultss/sys_log")
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler("resultss.log")
    fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    # create formatter and add it to the handlers
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)
    logger.info(erroinfo)
    a = auxiliary_module.Auxiliary()
    logger.info(successinfo)
#    logger.info("second 02")
#    a.do_something()
 #   logger.info("third 03")
#    logger.info("four 04")
#    auxiliary_module.some_function()
#    logger.info("done with auxiliary_module.some_function()")
#logsys("erro","good job")
