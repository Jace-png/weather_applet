import logging

logger = logging.getLogger('django')  #获取日志


class TestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response  # 必须写的
        logger.info('build TestMiddleware')


    def __call__(self,request):
        logger.info('TestMiddleware before request')
        response = self.get_response(request)
        logger.info('TestMiddleware after request')
        return response
