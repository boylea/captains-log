from django import forms

from .models import LogEntry, ToDoEntry

class LogEntryForm(forms.ModelForm):
    text = forms.CharField(label='Entry', widget=forms.TextInput)

    class Meta:
        model = LogEntry
        fields = ('text',)

class ToDoForm(forms.ModelForm):
    text = forms.CharField(label='Entry', widget=forms.TextInput)

    class Meta:
        model = ToDoEntry
        fields = ('text',)