from django.db import models
from users.models import CustomUser, Article


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comment')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comment')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-created_at',)
        
    def __str__(self):
        return self.content 
