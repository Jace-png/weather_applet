from django.urls import path
from juhe import views
import time
urlpatterns = [
    path('TIS', views.hellojuhe),
    path('res',views.testrequest),
    path('img',views.images),
    path('app',views.wx),
    path('imgc',views.ImageView.as_view()),
    path('respmixin',views.ImageText.as_view()),
    path('cooktest',views.CookiesTest.as_view()),
    path('cokrec',views.CookiesReceive.as_view()),
    path('authize',views.Authize.as_view()),
    path('hobby',views.UserView.as_view()),
    path('logout',views.Logout.as_view()),
    path('status',views.Status.as_view()),
    path('weather',views.Weather.as_view())


]
