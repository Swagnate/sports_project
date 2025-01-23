from django.shortcuts import render, redirect
from .models import Country
from .forms import CountryForm

def country_list(request):
    countries = Country.objects.all()
    return render(request, 'registration/country_list.html', {'countries': countries})

def country_create(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('country_list')
    else:
        form = CountryForm()
    return render(request, 'registration/country_form.html', {'form': form})