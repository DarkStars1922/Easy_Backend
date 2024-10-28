from django.db import models
from users.models import CustomUser,Article,Favorite
from comments.models import Comment
from likes.models import Like

# 通知类如下
class Notification(models.Model):
    sender = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='sender')
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='receiver')
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE,null=True,blank=True)
    like = models.ForeignKey(Like,on_delete=models.CASCADE,null=True,blank=True)
    favorite = models.ForeignKey(Favorite,on_delete=models.CASCADE,null=True,blank=True)
    content = models.TextField()
    tag = models.CharField(blank=True,max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    
    class Meta:
        # 先根据是否阅读排序，未读通知置顶；后根据通知发送时间逆序排序
        ordering = ('read','-created_at')
        
    def __str__(self):
        return self.content