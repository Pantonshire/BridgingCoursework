from django import forms
from . import models

class ManagePostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'content', 'published']
