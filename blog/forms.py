from django import forms
from .models import CommentBlog


class CommentFormBlog(forms.ModelForm):
    class Meta:
        model = CommentBlog
        fields = '__all__'
        exclude = ['article', 'author']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({
            'class': 'comment_input comment_textarea',
            'placeholder': 'Message',
            'required': 'required'
        })
        self.fields['name'].widget.attrs.update({
            'class': 'comment_input',
            'placeholder': 'Your Name',
            'required': 'required'
        })

