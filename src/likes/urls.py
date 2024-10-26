from django.urls import path
from . import views

app_name = 'likes'

urlpatterns=[
    # 点赞/取消点赞相关路径
    path('like/<int:article_id>/',views.like,name='like') ,
    path('unlike/<int:article_id>/',views.unlike,name='unlike') ,
]