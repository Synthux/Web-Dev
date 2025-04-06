from django import forms
from .models import Company, Vacancy, Position


class CompForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ["name", "description", "city", "address"]


class PosForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ["name", "description"]


class VacForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ["name", "description", "salary", "company", "position"]
