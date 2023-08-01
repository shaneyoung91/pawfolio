from django.forms import ModelForm
from .models import ReportCard

class ReportCardForm(ModelForm):
    class Meta:
        model = ReportCard
        fields = ['date', 'behavior', 'summary', 'fed', 'grade']

