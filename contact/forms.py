from django import forms
from .models import Contact, Newsletter


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'contact_input',
            'placeholder': 'Name',
            'required': 'required',
        })
        self.fields['message'].widget.attrs.update({
            'class': 'contact_input',
            'placeholder': 'Message',
            'style': 'height: auto',
        })


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'newsletter_input',
            'required': 'required',
        })