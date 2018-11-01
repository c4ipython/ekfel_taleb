
from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(required=True, label='الايميل')
    name = forms.CharField(required=True, label='الاسم')
    message = forms.CharField(widget=forms.Textarea, required=True, label='الرسالة')
