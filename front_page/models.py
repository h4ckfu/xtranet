from django.db import models

class FrontPage(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255)
    pubdate = models.DateTimeField()
    body = models.TextField()
