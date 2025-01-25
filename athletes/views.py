from django.shortcuts import render, redirect, get_object_or_404
from .models import Country, Discipline, Athlete
from .forms import CountryForm, DisciplineForm, AthleteForm

# Страны
def country_list(request):
    countries = Country.objects.all()
    return render(request, 'athletes/country_list.html', {'countries': countries})

def country_create(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('country_list')
    else:
        form = CountryForm()
    return render(request, 'athletes/country_form.html', {'form': form})

def country_edit(request, pk):
    country = get_object_or_404(Country, pk=pk)
    if request.method == 'POST':
        form = CountryForm(request.POST, instance=country)
        if form.is_valid():
            form.save()
            return redirect('country_list')
    else:
        form = CountryForm(instance=country)
    return render(request, 'athletes/country_form.html', {'form': form})

def country_delete(request, pk):
    country = get_object_or_404(Country, pk=pk)
    if request.method == 'POST':
        country.delete()
        return redirect('country_list')
    return render(request, 'athletes/country_confirm_delete.html', {'country': country})

# Дисциплины
def discipline_list(request):
    disciplines = Discipline.objects.all()
    return render(request, 'athletes/discipline_list.html', {'disciplines': disciplines})

def discipline_create(request):
    if request.method == 'POST':
        form = DisciplineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('discipline_list')
    else:
        form = DisciplineForm()
    return render(request, 'athletes/discipline_form.html', {'form': form})
