from django import forms
from .models import Country, Discipline, Athlete

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название страны'}),
        }

class DisciplineForm(forms.ModelForm):
    class Meta:
        model = Discipline
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название дисциплины'}),
        }

class AthleteForm(forms.ModelForm):
    class Meta:
        model = Athlete
        fields = ['name', 'country', 'disciplines']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя участника'}),
            'country': forms.Select(attrs={'class': 'form-control'}),
            'disciplines': forms.CheckboxSelectMultiple(),  
        }
