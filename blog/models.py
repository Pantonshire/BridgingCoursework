from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    path = models.CharField(max_length=255, unique=True, blank=False, null=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False, null=False)
    title = models.CharField(max_length=255, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    published = models.BooleanField(default=False, blank=False, null=False)
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "%s (by %s)" % (self.title, self.author.username)

    def summary(self):
        return self.content[:509] + "..." if len(self.content) > 512 else self.content
