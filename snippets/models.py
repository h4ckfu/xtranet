from django.db import models

class Snippets(models.Model):
    title = models.CharField(max_length=255)
    pubdate = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
