from django.db import models
from django.conf import settings
from django.contrib.auth.models import User,AbstractUser

# models中保存的是“类”，换言之这是一个对类型的定义

# 比如文章类，即对文章进行定义。具体而言，我们可以添加 “标题”、“内容”、“作者”等子项

# 对于用户类，由于django已经内置了一个强大的用户模型，因此我们无需从零开始实现
# 但内置功能一般无法满足我们的所有需求，此时我们有两个方案可以选择：
# 1.使用OneToOneField扩展用户模型，即新建一个类并与默认类进行关联；
# 2.创建一个继承AbstractUser的类，并在settings.py中进行修改，使得Django的默认认证系统指向我们创建的自定义模型
# 本框架采取的是更容易理解的方案二
# 用户类如下：
class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.username

# 文章类如下：
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.title

# 收藏夹类如下：
class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} 收藏了 {self.article.title}"
