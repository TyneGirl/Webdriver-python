#coding=utf-8
'''
Created on 2014年3月13日

@author: ting.liu
'''
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import os,time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import os,time
import socket
def rest(re):
    localIp=socket.gethostbyname(socket.gethostname())
    print localIp
    t=time.strftime('%Y-%m-%d %H:%M',time.localtime(time.time()))
    print t
    tes=[]
    tes.append("Ip地址为："+localIp+" , "+"时间："+t+", "+"结果："+re+ "\n")
    print tes
    try:
        fobj=open("result.txt",'a')
    except IOError:
        print"result.txt file open error"
    else:
        #file("./a.txt",'w').writelines(tes)
     #   fobj.write('\n'+tes)
        fobj.writelines(tes)
        fobj.close()
              
#rest(u"没有BUG")
