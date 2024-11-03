from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from pages.models import Member
from . models import Car

def cars_view(request):
    cars = Car.objects.all()
    paginator = Paginator(cars, 6)
    page = request.GET.get('page')
    paged = paginator.get_page(page)

    models = Car.objects.values_list('title', flat=True).distinct()
    cities = Car.objects.values_list('city', flat=True).distinct()
    years = titles = Car.objects.values_list('year', flat=True).distinct()
    types = Car.objects.values_list('body_type', flat=True).distinct()

    members = Member.objects.all()

    dict = {
        'models': models,
        'cities': cities,
        'years': years,
        'types': types,
        'cars': paged,
        'members': members,
    }

    return render(request, 'pages/cars.html', dict)

def details_view(request, id):
    car = get_object_or_404(Car, id=id)
    members = Member.objects.all()

    return render(request, 'pages/details.html', {'car': car, 'members': members})
