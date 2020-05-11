import logging
class TestFilter(logging.Filter):
    def filter(self,record):
        if 'hjq' in record.msg:
            return False
        return True