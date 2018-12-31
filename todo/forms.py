from django import forms

class updateForm(forms.Form):
    edit = forms.CharField(label='Edit Item', max_length=50)