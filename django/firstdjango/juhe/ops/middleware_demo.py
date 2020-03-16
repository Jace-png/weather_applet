import logging
import datetime,time


logger = logging.getLogger('django')  #获取Django日志
class TestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response  # 必须写的
        logger.info('build TestMiddleware')
    def __call__(self,request):
        logger.info('TestMiddleware before request')
        response = self.get_response(request)
        logger.info('TestMiddleware after request')
        return response


tatistics_logger = logging.getLogger('statistics')#获取tatistics日志
class Statistics_Middleware:
    def __init__(self, get_response):
        self.get_response = get_response  # 必须写的

    def __call__(self,request):
        beforetime=time.time()
        _befortime = time.localtime(beforetime)
        format_befortime = time.strftime('%Y-%m-%d %H:%M:%S', _befortime)

        response = self.get_response(request)

        aftertime = time.time()
        api = request.path
        _aftertime = time.localtime(aftertime)
        format_aftertime = time.strftime('%Y-%m-%d %H:%M:%S',_aftertime)

        Time_consuming = aftertime - beforetime
        messages = {
            'beforetime':beforetime,
            'aftertime':aftertime,
            'api':api,
            'Time-consuming':Time_consuming
        }
        print('TestMiddleware after request')
        tatistics_logger.info(repr(messages))
        return response