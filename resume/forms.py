from django import forms
from resume.models import Contact



class ContactForm(forms.ModelForm):
    
    class Meta():
        model = Contact
        fields='__all__'