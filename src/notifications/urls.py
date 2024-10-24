from django.urls import path
from . import views

app_name = 'notifications'
urlpatterns=[
    path('mailbox/',views.mailbox,name='user_mailbox'),
    path('mark_as_read/<int:notification_id>/',views.mark_as_read,name='read'),
    path('delete_notification/<int:notification_id>/',views.delete_notification,name='delete_notification'),
    path('clean_mailbox/',views.clean_mailbox,name='clean_mailbox'),
] 