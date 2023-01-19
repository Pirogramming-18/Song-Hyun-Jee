from django.db import models


class DevtoolList(models.Model):
    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=50)
    content = models.TextField()


class Post(models.Model):
    title = models.CharField(max_length=64)
    photo = models.ImageField(blank=True, upload_to='posts/%Y%m%d')
    content = models.TextField()
    devtools = models.ForeignKey(
        DevtoolList, on_delete=models.CASCADE)
    interest = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
