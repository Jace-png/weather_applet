from django.test import TestCase

# Create your tests here.
# # print(res)
# from juhe.models import User

# r = User.objects.get(nickname='Vis')
# print(r.nickname)
import os
import django
import random
#配置django运行环境
os.environ['DJANGO_SETTINGS_MODULE'] = 'firstdjango.settings'
django.setup()

#生成随机验证码
def ranstr(length):
    CHS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    salt = ''
    for i in range(length):
        salt += random.choice(CHS)
    return salt


#因为代码运行的顺序,导入models写在下面
from juhe.models import User

# 添加一个用户(两种方法)
def add_one():
    # 1
    user = User(openid = 'test_open_id', nickname='test_nickname')
    user.save()
    # 2
    # User.objects.create(openid = 'test_open_id2', nickname='test_nickname2')

# 增：批量bulk_create
def add_batch():
    new_user_list = []
    for i in range(10):
        open_id = ranstr(32)
        nickname = ranstr(10)
        user = User(open_id=open_id, nickname=nickname)
        new_user_list.append(user)
    User.objects.bulk_create(new_user_list)

# 查询
def get_one():
    user = User.objects.get(openid='test_open_id')
    print(user.nickname)

# 数据过滤
def get_filter():
    users = User.objects.filter(openid__contains='test_')
    # open_id__startswith
    # 大于: open_id__gt(greater than)
    # 小于: open_id__lt(little than)
    # 大于等于：open_id__gte(greater than equal)
    # 小于等于：open_id__lte(little than equal)
    print(users)

# 数据排序
def get_order():
    users = User.objects.order_by('openid')
    print(users)

# 连锁查询
# 和管道符类似
def get_chain():
    users = User.objects.filter(openid__contains='test_').order_by('openid')
    print(users)
# 改一个
def modify_one():
    user = User.objects.get(openid = 'test_open_id')
    user.nickname = 'modify_username'
    user.save()
# 批量改
def modify_batch():
    User.objects.filter(openid__contains='test_').update(nickname='modify_uname')

# #删除一个
def delete_one():
    User.objects.get(openid='test_open_id').delete()

# 批量删除
def delete_batch():
    User.objects.filter(nickname__contains='test_').delete()

# 全部删除
def delete_all():
    User.objects.all().delete()
    # User.objects.delete()
# 字符串拼接：Concat
from django.db.models import Value
from django.db.models.functions import Concat
# annotate创建对象的一个属性, Value,如果不是对象中原有属性
def concat_function():
    user = User.objects.filter(openid='oQ1zd4iOi43CHlDVdG_ZAq7u1-gE').annotate(
        # open_id=(open_id), nickname=(nickname)
        screen_name = Concat(
            Value('openid='),'openid',
            Value(', '),
            Value('nickname='),'nickname',) )[0]
    print('screen_name = ', user.screen_name)


# 字符串长度： Length
from django.db.models.functions import Length

def length_function():
    user = User.objects.filter(openid='oQ1zd4iOi43CHlDVdG_ZAq7u1-gE').annotate(
        open_id_length = Length('openid'))[0]
    print(user.open_id_length)

# 大小写函数Upper   Lower
from django.db.models.functions import Upper, Lower

def case_function():
    user = User.objects.filter(openid='test_open_id').annotate(
        upper_open_id=Upper('openid'),
        lower_open_id=Lower('openid')
    )[0]
    print('upper_open_id:', user.upper_open_id, ', lower_open_id:', user.lower_open_id)

# 日期处理函数Now()
# Now()
from app1.models import Article
from django.db.models.functions import Now

def now_function():
    # 当前日期之前发布的所有应用
    apps = Article.objects.filter(publish_date__lte=Now())
    for app in apps:
        print(app)

# 时间截断函数
# Trunc
from django.db.models import Count
from django.db.models.functions import Trunc


def trunc_function():
    # 打印每一天发布的应用数量
    app_per_day = Article.objects.annotate(publish_day=Trunc('publish_date', 'day'))\
        .values('publish_day')\
        .annotate(publish_num=Count('article_id'))

    for app in app_per_day:
        print('date:', app['publish_day'], ', publish num:', app['publish_num'])

if __name__ == '__main__':
    try:
        # add_one()
        # add_batch()
        # get_one()
        # get_filter()
        # get_order()
        # get_chain()
        # modify_one()
        # modify_batch()
        # delete_one()
        # delete_batch()
        # concat_function()
        # length_function()
        # case_function()
        # now_function()
        trunc_function()
    except Exception as e:
        print(e)
