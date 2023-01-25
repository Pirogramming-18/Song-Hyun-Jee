from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    like = models.IntegerField()
    comment = models.CharField(max_length=500)
    status = models.BooleanField(default=False)
# Create your models here.
