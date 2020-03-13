import os
import django
from firstdjango import settings

# 配置django运行环境
# os.environ['DJANGO_SETTINGS_MODULE'] = 'firstdjango.settings'
# django.setup()

from email.mime.text import MIMEText  # 定义邮件内容的类
import smtplib


def send_email():
    msg = MIMEText('邮箱通道测试哈哈哈哈哈哈哈哈哈哈哈', 'plain', 'UTF-8')  # 内容  描述plain:一般的(不能随便写)    编码
    msg['FROM'] = 'test'  # 发件人
    msg['Subject'] = "email test"  # 邮件主题
    receivers = ['emailname@qq.com']  # 接收人  数组 可以填多个人的邮箱
    # 获取SMTP服务的服务端
    server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_POST)
    server.set_debuglevel(1)
    # 登陆
    server.login(settings.EMAL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
    # 发送
    server.sendmail(settings.EMAIL_FROM, receivers, msg.as_string())
    server.close()







if __name__ == '__main__':
    send_email()

