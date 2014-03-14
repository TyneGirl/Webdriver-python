
# -*- coding: cp936 -*-
import smtplib
import mimetypes
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
to_list=["1152037739@qq.com",'19066367@qq.com']
def AutoSendMail(content,file1):
    msg = MIMEMultipart()
    msg['From'] = "ting.liu@starlight-sms.com"
    msg['To'] = ";".join(to_list)
    msg['Subject'] = "ting.liu"
    txt = MIMEText(content,'plain','gb2312')     
    msg.attach(txt)    
   # file1 = "D:\\svn_QA\Screeshot\sourcingsearch.jpg"
    image = MIMEImage(open(file1,'rb').read())
    image.add_header('Content-Disposition','attachment',filename=file1)
    msg.attach(image)    
    server = smtplib.SMTP()
    server.connect('smtp.qq.com')
    server.login("ting.liu@starlight-sms.com",'3652523ting')
    server.sendmail(msg['From'],msg['To'],msg.as_string())
    server.quit()
#AutoSendMail()