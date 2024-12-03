from django import forms

class ApplicationForm(forms.Form):
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    date = forms.DateField()
    email = forms.EmailField()
    occupation = forms.CharField(max_length=80)