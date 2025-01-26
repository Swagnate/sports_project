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

def discipline_edit(request, pk):
    discipline = get_object_or_404(Discipline, pk=pk)
    if request.method == 'POST':
        form = DisciplineForm(request.POST, instance=discipline)
        if form.is_valid():
            form.save()
            return redirect('discipline_list')
    else:
        form = DisciplineForm(instance=discipline)
    return render(request, 'athletes/discipline_form.html', {'form': form})

def discipline_delete(request, pk):
    discipline = get_object_or_404(Discipline, pk=pk)
    if request.method == 'POST':
        discipline.delete()
        return redirect('discipline_list')
    return render(request, 'athletes/discipline_confirm_delete.html', {'discipline': discipline})

# Участники
def athlete_list(request):
    athletes = Athlete.objects.all()
    return render(request, 'athletes/athlete_list.html', {'athletes': athletes})

def athlete_create(request):
    if request.method == 'POST':
        form = AthleteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('athlete_list')
    else:
        form = AthleteForm()
    return render(request, 'athletes/athlete_form.html', {'form': form})

def athlete_edit(request, pk):
    athlete = get_object_or_404(Athlete, pk=pk)
    if request.method == 'POST':
        form = AthleteForm(request.POST, instance=athlete)
        if form.is_valid():
            form.save()
            return redirect('athlete_list')
    else:
        form = AthleteForm(instance=athlete)
    return render(request, 'athletes/athlete_form.html', {'form': form})

def athlete_delete(request, pk):
    athlete = get_object_or_404(Athlete, pk=pk)
    if request.method == 'POST':
        athlete.delete()
        return redirect('athlete_list')
    return render(request, 'athletes/athlete_confirm_delete.html', {'athlete': athlete})