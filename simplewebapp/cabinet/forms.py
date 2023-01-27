from django import forms

CHOICES = [('1', 'SYN'), ('2', 'TCP'), ('3', 'UDP')]

class ScanForm(forms.Form):
    network = forms.CharField(max_length=18)
    host = forms.CharField(max_length=18)
    port = forms.CharField()
    scan_type = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)