from django import forms

class CSV_Form(forms.Form):
    file = forms.FileField()