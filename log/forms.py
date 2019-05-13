from django import forms

from .models import LogEntry

class LogEntryForm(forms.ModelForm):
    text = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = LogEntry
        fields = ('text',)