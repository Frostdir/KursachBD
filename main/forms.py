from .models import Comment
from django.forms import ModelForm, Textarea


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

        widgets = {
            'comment': Textarea(attrs={
            'class': 'form-control',
            "placeholder": "Добавить комментарий...",
            "style": "margin-left: 95px; width: 50vw; float: left;background: rgba(205, 214, 219, 0.3;"
            })
        }