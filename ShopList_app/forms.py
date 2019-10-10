from django import forms
from .models import NewList

class NewListForm(forms.ModelForm):
    class Meta:
        model = NewList
        fields = ["item"]