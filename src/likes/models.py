from django.db import models
from users.models import CustomUser,Article

# 赞 类如下
class Like(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}点赞了{self.article.title}"
