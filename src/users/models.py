from django.db import models
from django.conf import settings
from django.contrib.auth.models import User,AbstractUser
from django.urls import reverse
from django.core.files.storage import default_storage
from taggit.managers import TaggableManager

# 用户类如下：
class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.username
    
    # 删除用户头像
    def delete_avatar(self):
        if self.avatar:
            default_storage.delete(self.avatar.path)
            self.avatar = None
            self.save()
        

# 文章类如下：
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    tags = TaggableManager(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    favorite_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='article_picture/',null=True,blank=True)

    class Meta:
        # 按照创建和更新时间逆序排序
        ordering = ('-created_at','-updated_at',)
    
    def __str__(self):
        return self.title
    
    # 返回当前文章详情页面
    def get_absolute_url(self):
        return reverse('article_detail', args=[self.id])
    
    # 删除文章图片
    def delete_picture(self):
        if self.picture:
            default_storage.delete(self.picture.path)
            self.picture = None
            self.save()

# 收藏夹类如下：
class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} 收藏了 {self.article.title}"

# 黑名单类如下
class Blacklist(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='user')
    blocker = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='black_user')
    
    def __str__(self):
        return f"{self.user.username} 拉黑了 {self.blocker.username}" 
    
