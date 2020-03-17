from django.db import models
from tinymce.models import HTMLField
from martor.models import MartorField
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=60)
    content = MartorField()
    editor = models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to='articles/', blank=True)

    class Meta:
        ordering = ['id']