from django.db import models
from users.models import CustomUser,Article
from comments.models import Comment

# 通知类如下
class Notification(models.Model):
    sender = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='sender')
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='receiver')
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    
    class Meta:
        # 先根据是否阅读排序，未读通知置顶；后根据通知发送时间逆序排序
        ordering = ('read','-created_at')
        
    def __str__(self):
        return self.content