from django import forms
from .models import Company, Vacancy


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ["name", "description", "city", "address"]


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ["name", "description", "salary", "company"]
