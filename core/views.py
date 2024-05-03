from django.shortcuts import render
from cars.models import Car
from pages.models import Member

def search_view(request):
    models = Car.objects.values_list('title', flat=True).distinct()
    cities = Car.objects.values_list('city', flat=True).distinct()
    years = titles = Car.objects.values_list('year', flat=True).distinct()
    types = Car.objects.values_list('body_type', flat=True).distinct()

    cars = Car.objects.order_by('-created_date')
    members = Member.objects.all()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']

        if keyword:
            cars = cars.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model']

        if model:
            cars = cars.filter(title__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']

        if city:
            cars = cars.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']

        if year:
            cars = cars.filter(year__iexact=year)

    if 'type' in request.GET:
        body_type = request.GET['type']

        if body_type:
            cars = cars.filter(body_type__iexact=body_type)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']

        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)

    context = {
        'models': models,
        'cities': cities,
        'years': years,
        'types': types,
        'cars': cars,
        'members': members,
    }

    return render(request, 'pages/search.html', context)