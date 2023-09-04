#
#
#
#
#
from django import forms
from .models import ContactForm


class ContactFormData(forms.ModelForm):

    class Meta:
        model = ContactForm
        fields = ['nume', 'email', 'phone', 'message']
