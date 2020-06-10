from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    published = models.BooleanField(default=False, null=False)
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "%s by %s" % (self.title, self.author.username)
