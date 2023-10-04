from .models import green_table
from django import forms

class greenForm(forms.ModelForm):
    class Meta:
        model = green_table
        fields = ['name','desc','date','img']