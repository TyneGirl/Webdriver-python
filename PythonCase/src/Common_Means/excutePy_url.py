#coding=utf-8
'''
Created on 2014��2��25��

@author: ting.liu
'''
#coding=utf-8
'''
Created on 2014��2��13��

@author: ting.liu
'''
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os,time
from Affiliate_test import Means
from Affiliate_test import New_Souring
import logging
import sys
import thread
import dummy_thread
from PyQt4.QtGui import *
from PyQt4.QtCore import *

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
h_ok = thread.allocate_lock() 
class StandardDialog(QDialog):  
    global flag,i

    def __init__(self,parent=None):  
        super(StandardDialog,self).__init__(parent)          
        self.setWindowTitle("Standard Dialog")  
        self.setStyleSheet("background-image:url(image/test03.jpg)")
        NewSourcing=QPushButton(self.tr("New Sourcing"))  
        pausebutton=QPushButton(self.tr("Pause"))
        newaffiliate=QPushButton(self.tr("New Affiliate"))  
        fontPushButton=QPushButton(self.tr("字体对话框"))  
        filePushButton01=QPushButton(self.tr("AffiliateLink测试按钮01")) 
         
        self.fileLineEdit=QLineEdit()  
        self.colorFrame=QFrame()  
        self.colorFrame.setFrameShape(QFrame.Box)
          
        self.colorFrame.setAutoFillBackground(True)  
        self.fontLineEdit=QLineEdit("Hello World!")  
           
        layout=QGridLayout()  
        layout.addWidget(NewSourcing,0,0)
  #      filePushButton.setFixedSize(QtCore.QSize(50,50))  
        NewSourcing.setStyleSheet("QPushButton{color:red;background:pink} QPushButton:hover{color:blue}")
       # filePushButton.setStyleSheet("QPushButton{background-image:url(image/test03.jpg);background-repeat: repeat-xy;background-position: center;background-attachment: fixed;background-attachment: fixed;background-attachment: fixed;;background-clip: padding}");

        layout.addWidget(pausebutton,0,1)
       # layout.addWidget(self.fileLineEdit,0,1)  
        layout.addWidget(newaffiliate,1,0) 
        newaffiliate.setStyleSheet("QPushButton{color:red;background:pink} QPushButton:hover{color:blue}") 
        #layout.addWidget(self.colorFrame,1,1)  
        layout.addWidget(fontPushButton,2,0)  
        layout.addWidget(self.fontLineEdit,2,1)  
      #  self.setStyle('''background-color:red;''')
  
        self.setLayout(layout)  
  
        self.connect(NewSourcing,SIGNAL("clicked()"),self.newsourcing)
        self.connect(pausebutton,SIGNAL("clicked()"),self.puse)  
        #self.connect(colorPushButton,SIGNAL("clicked()"),self.openColor)  
        self.connect(fontPushButton,SIGNAL("clicked()"),self.openFont)  
        self.resize(500,500)
        

    def newsourcing(self):  
        #flag=2
      #  i=int(flag)
      #  if 0==i%2: 
        #os.system('python E:\eclipse\PythonCase1\src\Affiliate_test\AffiliateLink.py')
        #os.popen('notepad')
       #print "test ok"
        #Thread(target=New_Souring.nessouring, args=()).start()
        
        thread.start_new_thread(New_Souring.nessouring,())
        
        
        
       # AffiliateLink.Test01(None);
          # i=i+1
       # else:
        #   sys.exit()
        #    os.system("pause")

        
    def puse(self):
        
        exit()
        
    def openFont(self):  
     
        f,ok=QFontDialog.getFont()  
        if ok:  
            self.fontLineEdit.setFont(f)  

app=QApplication(sys.argv)  
form=StandardDialog()  
form.show()  
app.exec_()  
