from django import forms
from django.forms.widgets import DateInput

CATS = [
    ('1', 'cat1'),
    ('2', 'cat2')
]
DATE_INPUT_FORMATS = ['%d-%m-%Y']
class FormName(forms.Form) :
    name = forms.CharField()
    start_date = forms.DateField(widget=DateInput({'class': 'datepicker'}))
    end_date = forms.DateField(widget=DateInput({'class': 'datepicker'}))
    category = forms.ChoiceField(
        widget=forms.Select, choices=CATS
    )