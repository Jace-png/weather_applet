from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponse, JsonResponse, FileResponse
import requests, yaml, os
from firstdjango import settings
from Utils.resputils import ResponseMixin, SavePicMixin,Code
import hashlib,time,json
from juhe.static.wxappid import openid_secret
from juhe.models import User


def hellojuhe(request):
    times = time.time()
    times = str(times)
    nowtime = times[:10]
    # res = requests.get('http://api.juheapi.com/japi/toh?v=1.0&month=2&day=24&key=287fbfa6538667bb8680840a136a3a9e')
    res = requests.get('http://v.juhe.cn/joke/content/list.php?key=8b60f927442f3cc02d849e63dc456f13&time='+nowtime+'&sort=desc&pagesize=5')
    if res.status_code == 200:
        # resjson = json.dumps(res.text)
        return HttpResponse(res.text)
    return HttpResponse('数据没有获取')


def testrequest(request):
    res_method = request.method  # 请求方法
    res_client = request.META  # 客户端信息
    res_get = request.GET  # get请求参数
    res_headers = request.headers.__str__()  # 请求头
    res_cookie = request.COOKIES  # cookies
    return render(request, 'juhe/res_test.html',
                  {"res_method": res_method, "res_client": res_client, "res_get": res_get, "res_headers": res_headers,
                   "res_cookie": res_cookie})


# 函数视图
def images(request):
    if request.method == 'GET':
        image_path = os.path.join(settings.SRTATIC_URL_SELF, 'images', '02.jpg')
        with open(image_path, 'rb') as f:
            return HttpResponse(content=f.read(), content_type='image/jpeg')
    elif request.method == 'POST':
        return HttpResponse('这是post请求')
    else:
        return HttpResponse(request.method + '没有实现')


# 类视图
class ImageView(View, SavePicMixin, ResponseMixin,Code):
    def get(self, request):
        image_path = os.path.join(settings.SRTATIC_URL_SELF, '01.jpg')
        with open(image_path, 'rb')as f:
            return HttpResponse(f.read(), content_type='image/jpeg')
        # return render(request,'juhe/imgs.html')
    def post(self, request):
        resfile = request.FILES
        response = []
        for k, v in resfile.items():
            picontent = v.read()
            filename_md5 = hashlib.md5(picontent).hexdigest()
            path = filename_md5+'.jpg'
            SavePicMixin.savepic(filename=path, filecontent=picontent)
            response.append({
                'name':k,
                'filename_md5':filename_md5,
                'code': Code.SUCCESS
            })
            return JsonResponse(data=self.wrap_response({
                'response':response
            }))
        else:
            return JsonResponse(data=self.wrap_response(
                {'fail to upload': 'fail to upload',
                 "code": Code.FAILED}))

    def delete(self,request):
        md5 = request.GET.get('filename_md5')
        imagename = md5+'.jpg'
        path = os.path.join(settings.SRTATIC_URL_SELF,imagename)
        if os.path.exists(path):
            os.remove(path)
            message = "remove success"
        else:
            message = 'file %s not found'%imagename
        return HttpResponse(message)


def wx(request):
    filepath = r"D:\firstdjango\firstdjango\myappconfig.yaml"
    with open(filepath, 'r', encoding='utf8')as f:
        res = yaml.load(f, Loader=yaml.FullLoader)
        print(res)
    return JsonResponse(res)


# Mixin
class ImageText(View, ResponseMixin):
    def get(self, request):
        return JsonResponse(data=self.wrap_response({'url': 'xxxxx', 'abc': '我很好', 'code': 2222}))

#cookies 发送cookies
class CookiesTest(View):
    def get(self,request):
        request.session['mykey']='my_key'
        return  JsonResponse({'key':'value'})
#接收cookies
class CookiesReceive(View):
    def get(self,request):
        print(request.session['mykey'])
        print(request.session.items())
        return  JsonResponse({'key2':'value2'})





#登陆认证,保存用户信息
class Authize(View):
    def get(self,request):
        return render(request,"juhe/404.html")
    def post(self,request):
        # if not already_authorized(request):
        #     return JsonResponse({'key': '没登录认证'}, safe=False)
        # 微信发给后台的code 存在于body中
        #body中的code是字节流 需要换为str
        bodystr = request.body.decode('utf-8')
        #因为请求的code最终要是dict 所以用json转换为dict
        bodydict = json.loads(bodystr)
        code = bodydict.get('code')
        userinfo = bodydict.get('nickname')
        print(code,userinfo)
        #发起请求
        # 微信小程序的appid
        appids = openid_secret.appid
        #微信小程序的secret_key
        secret = openid_secret.secret
        #微信发送给后台的code
        js_code = code
        url='https://api.weixin.qq.com/sns/jscode2session?appid={}&secret={}&js_code={}&grant_type=authorization_code'.format(appids,secret,js_code)
        res = requests.get(url)
        print(res.text)
        res_dict = json.loads(res.text)
        openid = res_dict.get('openid')
        if not openid:
            return HttpResponse('认证失败')
        #用户状态
        request.session['openid'] = openid
        request.session['is_authorized'] = True
        if not User.objects.filter(openid=openid):
            newuser = User(openid=openid,nickname=userinfo)
            newuser.save()
        return HttpResponse('认证成功')

# 判断是否已经授权
def already_authorized(request):
    is_authorized = False
    if request.session.get('is_authorized'):
        is_authorized = True
    return is_authorized
class UserView(View):
    # 关注的城市、股票和星座
    def get(self, request):
        if not already_authorized(request):
            return JsonResponse({'key':'没登录认证'}, safe=False)
        openid = request.session.get('openid')
        print(openid,'openid-----------------')
        user = User.objects.get(openid=openid)
        data = {}
        data['focus'] = {}
        data['focus']['city'] = json.loads(user.city)
        data['focus']['stock'] = json.loads(user.stock)
        data['focus']['constellation'] = json.loads(user.constellation)
        return JsonResponse(data=data, safe=False)
    def post(self, request):
        if not already_authorized(request):
            return JsonResponse({'key': '没登录认证'}, safe=False)
        openid = request.session.get('openid')
        # print('openid',openid)
        #从数据库获取到openid
        user = User.objects.get(openid=openid)
        #解码获取到的body的内容
        received_body = request.body.decode('utf-8')
        #转换为字典
        received_body = eval(received_body)
        cities = received_body.get('city')
        stocks = received_body.get('stock')
        constellations = received_body.get('constellation')
        # print({'received_body':received_body})

        #  不是追加的形式,是覆盖原有纪录

        #     以json格式存入数据库
        if cities:
            user.city = json.dumps(cities)
            # user.city = cities
            user.save()
        elif stocks:
            user.stock = json.dumps(stocks)
            # user.stock = stocks
            user.save()
        elif constellations:
            user.constellation = json.dumps(constellations)
            # user.constellation = constellations
            user.save()
        else:
            return HttpResponse('获取到的{}为空'.format(cities,stocks,constellations))
        # 类名.objects.get(pk=id)
        u = User.objects.get(openid=openid)
        print(u.city,u.stock,u.constellation)
        return JsonResponse(data={'msg':'成功了'}, safe=False)

class Logout(View):
    def get(self,request):
        request.session.clear()
        return JsonResponse(data={"status":"Logout"},safe=False)

class Status(View):
    def get(self,request):
        if already_authorized(request):
            data = ({'is_authorized':1})
        else:
            data = ({'is_authorized':0})
        return JsonResponse(data=data,safe=False)


def weather(cityname):

    key =openid_secret.juweatherid 
    api = openid_secret.juweatherapi
    params = 'city=%s&key=%s' % (cityname[0:2], key)
    url = api + '?' + params
    print(url)
    response = requests.get(url=url)
    data = json.loads(response.text)
    print(data)
    result = data.get('result')
    realtime = result.get('realtime')
    response = {}
    response['temperature'] = realtime.get('temperature')  #温度
    response['wid'] = realtime.get('wid') # 风况
    response['humidity'] = realtime.get('humidity')  #湿度
    response['power'] = realtime.get('power')  #风力
    response['info'] = realtime.get('info')  #天气信息
    return response


class Weather(View):
    def get(self, request):
        if not already_authorized(request):
            response = {'key':2500}
        else:
            data = []
            openid = request.session.get('openid')
            user = User.objects.filter(openid=openid)[0]
            cities = json.loads(user.city)
            for city in cities:
                result = weather(city.get('city'))
                result['city_info'] = city
                data.append(result)
            response = data
        return JsonResponse(data=response, safe=False)


    def post(self, request):
        data = []
        received_body = request.body.decode('utf-8')
        received_body = json.loads(received_body)
        print(received_body)
        cities = received_body.get('cities')
        for city in cities:
            result = weather(city.get('city'))
            result['city_info'] = city
            data.append(result)
        response_data = {'key':'post..'}
        return JsonResponse(data=response_data, safe=False)


