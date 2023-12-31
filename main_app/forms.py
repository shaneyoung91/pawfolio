from django import forms
from django.forms import ModelForm
from .models import ReportCard, Treat

class ReportCardForm(ModelForm):
    photo_file = forms.ImageField(required=False)
    class Meta:
        model = ReportCard
        fields = ['date', 'behavior', 'summary', 'fed', 'grade']


# CIRCLE BACK - ADDING DOG TREAT ON DOG INDEX PAGE
class TreatForm(ModelForm):
    class Meta:
        model = Treat
        fields = ['name', 'flavor']
#  -------------------------------