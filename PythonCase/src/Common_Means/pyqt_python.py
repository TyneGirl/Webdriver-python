#coding=utf-8
'''
Created on 2014骞�鏈�5鏃�

@author: jing.liu
'''
#coding=utf-8
'''
Created on 2014年02月25号
@author: ting.liu
'''
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os,time
from Affiliate_test import Means
import logging
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import excutePy_url
'''
a=QApplication(sys.argv)
b=QPushButton("hello kitty")
b.show()
a.connect(b,SIGNAL("clicked()"),a,SLOT("quit()"))  
a.exec_()

#dr=webdriver.Firefox()
#dr.get("http://192.168.1.20:9999")

#Means.login(dr,'0@cm.com', '123456')
'''
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))  
  
class StandardDialog(QDialog):  
  
    def __init__(self,parent=None):  
        super(StandardDialog,self).__init__(parent)  
        py_url=excutePy_url.excutePy()
          
        self.setWindowTitle("Standard Dialog")  
          
        filePushButton=QPushButton(self.tr("AffiliateLinkd"))  
        colorPushButton=QPushButton(self.tr("gtood")) 
        fontPushButton=QPushButton(self.tr("test")) 
        filePushButton01=QPushButton(self.tr("newsorcing"))
        
        self.fileLineEdit=QLineEdit()  
        self.colorFrame=QFrame()  
        self.colorFrame.setFrameShape(QFrame.Box)  
        self.colorFrame.setAutoFillBackground(True)  
        self.fontLineEdit=QLineEdit("Hello World!")  
  
        layout=QGridLayout()  
        layout.addWidget(filePushButton,0,0) 
        layout.addWidget(filePushButton01,0,1) 
 #       layout.addWidget(self.fileLineEdit,0,1)  
        layout.addWidget(colorPushButton,1,0)  
        layout.addWidget(self.colorFrame,1,1)  
        layout.addWidget(fontPushButton,2,0)  
        layout.addWidget(self.fontLineEdit,2,1)  
  
        self.setLayout(layout)  
  
        self.connect(filePushButton,SIGNAL("clicked()"),self.button)  
        self.connect(filePushButton,SIGNAL("clicked()"),self.button) 
       # self.connect(fontPushButton,SIGNAL("clicked()"),self.openFont)  
        self.resize(500,500)
    
    def button(self):  
          
        os.system('python E:\eclipse\PythonCase\src\Affiliate_test\AffiliateLink.py')
        
  
app=QApplication(sys.argv)  
form=StandardDialog()  
form.show()  
app.exec_()  