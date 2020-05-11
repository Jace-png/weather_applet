import logging
import datetime
from juhe.ops import log_email
logger = logging.getLogger('django')
def demo():
    message = 'job log in crontab,now time is :'+str(datetime.datetime.now())

    logger.info(message)

def analysis_cron():
    cron = log_email.send_email()
    return cron