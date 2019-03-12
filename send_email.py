#! -*- coding:utf-8 -*-

from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import smtplib
import glob
import os

def send_email(toaddrs,subject,content,file_name=None,file_dir=None):
	'''
	自动发邮件，需要传入几个参数
	'''
	fromaddr = "fromaddr" #自己的邮箱
	smtpaddr = "smtp.exmail.qq.com"
	toaddrs = toaddrs #发送给哪些人，传入list
	subject = subject
	password = "password" #邮箱密码

	mail_msg = MIMEMultipart()
	mail_msg['Subject'] = subject #传入的标题
	mail_msg['From'] = fromaddr
	mail_msg['To'] = ','.join(toaddrs)
	mail_msg.attach(MIMEText(content, 'plain', 'utf-8')) #邮件正文
	if file_dir == None:
		part = MIMEApplication(open(file_name,'rb').read(),'utf-8')
		part.add_header('Content-Disposition', 'attachment', filename=('gbk','',os.path.split(file_name)[-1]))
		mail_msg.attach(part)
	else:
		file_names = glob.glob(r'{0}\*.*'.format(file_dir))
		for file_name in file_names:
			part = MIMEApplication(open(file_name,'rb').read(),'utf-8')
			part.add_header('Content-Disposition', 'attachment', filename=('gbk','',os.path.split(file_name)[-1]))
			mail_msg.attach(part)

	try:
		s = smtplib.SMTP()
		print(1)
		s.connect(smtpaddr)  # 连接smtp服务器
		print(2)
		s.login(fromaddr, password)  # 登录邮箱
		print(3)
		s.sendmail(fromaddr, toaddrs, mail_msg.as_string())  # 发送邮件
		print(4)
		s.quit()
		print(u'发送成功')
	except Exception as e:
		print("Error: unable to send email")
		print(traceback.format_exc())
