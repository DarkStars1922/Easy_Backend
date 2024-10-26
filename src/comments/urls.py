from django.urls import path
from . import views

app_name='comments'
urlpatterns=[
    # 评论相关路径
    path('post_comment/<int:article_id>/',views.post_comment,name = 'post_comment'),
    path('delete_comment/<int:comment_id>/',views.delete_comment,name='delete_comment'),
]