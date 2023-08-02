from django.forms import ModelForm
from .models import ReportCard, Treat

class ReportCardForm(ModelForm):
    class Meta:
        model = ReportCard
        fields = ['date', 'behavior', 'summary', 'fed', 'grade']

class TreatForm(ModelForm):
    class Meta:
        model = Treat
        fields = ['name', 'flavor']