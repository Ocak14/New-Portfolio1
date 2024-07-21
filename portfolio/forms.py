from django.forms import ModelForm
from django import forms
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "content"]

    def clean(self):
        cleaned_data = super().clean()

        name = cleaned_data.get('name')
        content = cleaned_data.get('content')

        if name:
            if len(name) < 3:
                self.add_error('name', 'Minimum 3 characters required')
        else:
            self.add_error('name', 'Name is required')

        if content:
            if len(content) < 10:
                self.add_error('content', 'Post should contain a minimum of 10 characters')
        else:
            self.add_error('content', 'Content is required')

        return cleaned_data
