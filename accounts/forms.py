from django import forms
from accounts.models import Students
from accounts.models import Sponsor


class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['username', 'password', 'full_name', 'age', 'birth_date', 'number', 'city', 'img', 'stage']


class SponsorForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = ['username', 'password', 'full_name', 'age', 'birth_date', 'number', 'city', 'img', 'work', 'work_locations', 'salary']
