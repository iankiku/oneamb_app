from django import forms
from .models import TodoItem
from django.forms import ModelForm




class InputForm(forms.ModelForm):
        # model = TodoItem

        content = forms.CharField(label='Edit Item', max_length=50)
        # class Meta:
        #         model = TodoItem,
        #         fields = ("content",)
