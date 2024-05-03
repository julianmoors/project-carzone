from django.shortcuts import render

from cars.models import Car
from . models import Member

def home_view(request):
    models = Car.objects.values_list('title', flat=True).distinct()
    cities = Car.objects.values_list('city', flat=True).distinct()
    years = titles = Car.objects.values_list('year', flat=True).distinct()
    types = Car.objects.values_list('body_type', flat=True).distinct()

    cars = Car.objects.order_by('-created_date')[:6:1]
    members = Member.objects.all()

    context = {
        'models': models,
        'cities': cities,
        'years': years,
        'types': types,
        'cars': cars,
        'members': members,
    }

    return render(request, 'pages/home.html', context)

def about_view(request):
    members = Member.objects.all()
    return render(request, 'pages/about.html', {'members': members})

def services_view(request):
    members = Member.objects.all()
    return render(request, 'pages/services.html', {'members': members})

def contact_view(request):
    members = Member.objects.all()
    return render(request, 'pages/contact.html', {'members': members})
