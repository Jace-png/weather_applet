import django
import os
import time

# 配置django运行环境
os.environ['DJANGO_SETTINGS_MODULE'] = 'firstdjango.settings'
django.setup()

from django.core.cache import cache


# def basic_use():
#     s = 'hahahahahah'
#     cache.set('key',s,5)
#     cache_result = cache.get('key')
#     print(cache_result)
#     time.sleep(6)
#     cache_result = cache.get('key')
#     print(cache_result)

def get_cache(str):
    return cache.get(str)


def set_cache(k, v):
    cache.set(k, v)


def main(data):
    res = get_cache(data)
    if res:
        print('前面的', res)
    else:
        print('正在设置' + data)
        datatype = data[2:]
        set_cache(datatype, data)
        res = get_cache(datatype)
        print('后面设置的', res)
    return res


if __name__ == '__main__':
    # main('百事可乐')
    res = get_cache('可乐')
    print(res)
