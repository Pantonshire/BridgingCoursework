import re
from unicodedata import name
from django.db import models
from django.conf import settings
from django.utils import timezone
from . import constants

class Post(models.Model):
    path = models.CharField(max_length=255, unique=True, blank=False, null=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False, null=False)
    title = models.CharField(max_length=255, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    published = models.BooleanField(default=False, blank=False, null=False)
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '%s (by %s)' % (self.title, self.author.username)

    def summary(self):
        if len(self.content) > constants.post_preview_character_limit:
            return self.content[: constants.post_preview_character_limit - 3] + '...'
        else:
            return self.content

    def update_time(self):
        self.date = timezone.now()

    def update_path(self):
        path = self.title.lower().strip()
        path = re.sub(r'\s+', '-', path)
        path = re.sub(r'[^a-z0-9-]', '', path)
        if len(path) == 0:
            path = 'post'
        unqiue_path = path
        number = 1
        while True:
            if Post.objects.filter(path=unqiue_path).count() == 0:
                break
            number += 1
            unqiue_path = '%s-%d' % (path, number)
        self.path = unqiue_path

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return 'Comment #%d for post: "%s"' % (self.id, self.post)
