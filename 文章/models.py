from django.db import models

# Create your models here.

class 文章(models.Model):
    标题 = models.CharField(max_length=255)
    内容 = models.CharField(max_length=255)