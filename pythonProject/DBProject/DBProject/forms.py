from django import forms
from A2.models import Link



class LinkForm(forms.ModelForm):
    institute = forms.CharField(required=0,max_length=30)
    dept = forms.CharField(required=0,max_length=30)
    course = forms.CharField(required=0,max_length=30)
    password = forms.CharField(required=0,max_length=30)
    class Meta:
        model = Link
        fields = (
            'institute',
            'dept',
            'course',
            'password'
        )