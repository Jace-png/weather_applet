from django.contrib import admin
from juhe.models import User
import time
# Register your models here.
# admin.site.register(User)
@admin.register(User)
class AuthorizationUserAdmin(admin.ModelAdmin):
    exclude = ['openid']  #屏蔽那些信息
    fields = ['nickname','city','stock','constellation'] #指定显示那些信息
    def save_model(self, request, obj, form, change):
        openid = obj.nickname + str(time.time())

        obj.openid = openid
        super().save_model(request,obj,form,change)
