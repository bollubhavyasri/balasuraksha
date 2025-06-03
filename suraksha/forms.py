# forms.py
from django import forms
from .models import IncidentReport

# Incident report form for saving to DB
class ReportForm(forms.ModelForm):
    class Meta:
        model = IncidentReport
        fields = ['name', 'email', 'relationship', 'victim_name', 'location', 'description', 'proof_files']

# Parent email form for reporting to parent
class EmailReportForm(forms.Form):
    victim_email = forms.EmailField(label="Victim's Email")
    parent_email = forms.EmailField(label="Parent's Email")
    message = forms.CharField(label="Message", widget=forms.Textarea)
