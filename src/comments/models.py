from django.db import models
from users.models import CustomUser, Article

# 评论类如下
class Comment(models.Model):
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comment')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comment')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        # 按照创建时间逆序排序
        ordering = ('-created_at',)
        
    def __str__(self):
        return self.content 
