from django.urls import path
from . import views

app_name = 'likes'

urlpatterns=[
    path('like/<int:article_id>/',views.like,name='like') ,
    path('unlike/<int:article_id>/',views.unlike,name='unlike') ,
]