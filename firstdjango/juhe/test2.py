import django
import os

#配置django运行环境
os.environ['DJANGO_SETTINGS_MODULE'] = 'firstdjango.settings'
django.setup()

from timeit import Timer
from juhe.models import User,App
# user1 = User.objects.all()[0]
# print(user1.menu)
#懒加载
def lazy_load():
    for user in User.objects.all():
        print(user.menu.all())
#预加载
def pre_load():
    for user in User.objects.prefetch_related('menu'):
        print(user.menu.all())
#
# if __name__ == '__main__':
#     lazy_time = Timer("lazy_load()","from __main__ import lazy_load")
#     pre_time = Timer("pre_load()","from __main__ import pre_load")
#     print('懒加载:',lazy_time.timeit(1000),'预加载:',pre_time.timeit(1000))
