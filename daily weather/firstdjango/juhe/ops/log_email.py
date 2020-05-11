# 分析日志 发送至邮箱(定时任务)

# 格式: {path:[访问次数,最大连接时间,最少连接时间,总链接时长,平均连接时间],path:[],.......}

from juhe.static.wxappid import openid_secret
from firstdjango import settings
from email.mime.text import MIMEText
import smtplib

# 日志文件路径
path = settings.LOG_DIR + '\Access_statistics.log'


# api:

def analysis_log():
    result = {}
    with open(path, 'r', encoding='utf-8')as f:
        for lins in f:
            lins = eval(lins)  # 一行转字典
            if lins['api'] in result:
                # 统计请求次数
                result[lins['api']][0] += 1
                print(result[lins['api']][0],'--111-',result[lins['api']])
                print(result,'-------sss')
                # 最大连接时间
                if lins['Time-consuming'] > result[lins['api']][1]:
                    result[lins['api']][1] = lins['Time-consuming']
                # 最小连接时间
                if lins['Time-consuming'] < result[lins['api']][2]:
                    result[lins['api']][2] = lins['Time-consuming']
                # 总连接时间
                result[lins['api']][3] += lins['Time-consuming']
                # 平均连接时间
                result[lins['api']][4] = result[lins['api']][3] / result[lins['api']][0]

            else:
                res = []
                res.append(1)
                res.append(lins['Time-consuming'])
                res.append(lins['Time-consuming'])
                res.append(lins['Time-consuming'])
                res.append(lins['Time-consuming'])
                result[lins['api']] = res

    return result


def send_email():
    # 邮件内容
    msg = MIMEText(repr(analysis_log()), "plain", "utf-8")
    # 发件人
    msg['FROM'] = "Shark Chili"
    # 邮件主题
    msg['Subject'] = "【API 请求时间统计】"
    # 邮件接收者
    receivers = [openid_secret.Email]
    # 不加密
    # server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
    # 加密
    server = smtplib.SMTP_SSL(settings.EMAIL_HOST, settings.EMAIL_POST)
    server.set_debuglevel(1)
    server.login(settings.EMAL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
    server.sendmail(settings.EMAIL_FROM, receivers, msg.as_string())
    server.close()


if __name__ == '__main__':
    send_email()
    # print(analysis_log())
