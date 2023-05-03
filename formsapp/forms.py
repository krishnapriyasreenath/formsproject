from django import forms
from formsapp.models import employee
class employeeforms(forms.ModelForm):
    class Meta:
        model= employee
        fields='__all__'