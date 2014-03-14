#coding=utf-8
import smtplib  
from email.mime.text import MIMEText  
from email.mime.image import MIMEImage
mailto_list=["19066367@qq.com","1152037739@qq.com"]
mail_host="smtp.qq.com"  #设置服务器
mail_user="ting.liu@starlight-sms.com"    #用户名
mail_pass="3652523ting"   #口令 
mail_postfix="qq.com"  #发件箱的后缀
  
def send_mail(to_list,sub,content):  
    me="liuting"+"<"+mail_user+"@"+mail_postfix+">"  
    msg = MIMEText(content,_subtype='plain',_charset='gb2312')  
    msg['Subject'] = sub  
    msg['From'] = me  
    msg['To'] = ";".join(to_list)  
    try:  
        server = smtplib.SMTP_SSL()  
        server.connect(mail_host)  
        server.login(mail_user,mail_pass)  
        server.sendmail(me, to_list, msg.as_string())  
        server.close()  
        return True  
    except Exception, e:  
        print str(e)  
        return False 
""""
if __name__ == '__main__':  
    if send_mail(mailto_list,"Slenium test send email","just test it\！"):  
        print "发送成功"  
    else:  
        print "发送失败"
    """