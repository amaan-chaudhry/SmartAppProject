from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50, default='SOME STRING')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content= models.TextField()
    def __str__(self):
        return self.title
