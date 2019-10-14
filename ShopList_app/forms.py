from django import forms
from .models import List

class NewListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['list_name']

