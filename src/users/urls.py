from django.urls import path
from . import views

urlpatterns = [
    # 用户相关路径
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('email_login/',views.email_login,name='email_login'),
    path('logout/', views.user_logout, name='logout'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('home/', views.user_home, name='user_home'),
    # 文章相关路径
    path('article/create/', views.create_article, name='create_article'),
    path('article/<int:article_id>/update/', views.update_article, name='update_article'),
    path('article/<int:article_id>/delete/', views.delete_article, name='delete_article'),
    path('article/<int:article_id>/favorite/', views.favorite_article, name='favorite_article'),
    # 文章列表及文章详情路径
    path('articles/', views.article_list, name='article_list'),
    path('articles/<int:article_id>/', views.article_detail, name='article_detail'),
    # 黑名单相关路径
    path('blacklists/create/<int:comment_id>/',views.create_blacklist,name='create_blacklist'),
    path('blacklists/<int:blacklist_id>/delete/',views.delete_blacklist,name='delete_blacklist'),
]
