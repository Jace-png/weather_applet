from django.urls import path
from app1 import views

urlpatterns = [
    path('hello', views.index),
    path('content', views.acticle_content),
    path('blog', views.show_templates),
    path('info/<int:article_id>',views.show_bloginfo),
    path('image',views.image_info)
]
