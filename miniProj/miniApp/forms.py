from django import forms
from .models import TimeCardModel


class TimeCardForm(forms.ModelForm):
    class Meta():
        model = TimeCardModel
        fields = '__all__'
