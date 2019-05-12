from django import forms

from .models import LogItem

class LogItemForm(forms.ModelForm):
    text = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = LogItem
        fields = ('text',)