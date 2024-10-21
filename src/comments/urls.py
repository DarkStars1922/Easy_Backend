from django.urls import path
from . import views

urlpatterns=[
    path('post_comment/<int:article_id>/',views.post_comment,name = 'comment'),
]