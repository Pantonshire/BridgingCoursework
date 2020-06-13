from django import forms
from . import models

class ManagePostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'content', 'published']

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
        }
