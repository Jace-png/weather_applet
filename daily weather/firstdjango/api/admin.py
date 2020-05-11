from django.contrib import admin
from api.models import App


# Register your models here.


# 注册模型
# admin.site.register(App)
import hashlib
@admin.register(App)
class AuthorizationUserAdmin(admin.ModelAdmin):
    exclude = ['appid']  # 屏蔽那些信息
    fields = ['category', 'application', 'name', 'publish_date', 'url', 'desc']  # 指定显示那些信息

    def save_model(self, request, obj, form, change):
        src = obj.category + obj.application
        appid = hashlib.md5(src.encode('utf-8')).hexdigest()
        obj.appid = appid
        super().save_model(request,obj,form,change)
