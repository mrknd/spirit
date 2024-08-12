from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils.html import strip_tags

from cars.models import Car


def cars(request):
    cars = Car.objects.all().order_by('-created_at')
    paginator = Paginator(cars, 16)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    model_search = Car.objects.values_list('model', flat=True).distinct()
    fuel_type_search = Car.objects.values_list('fuel_type', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct().order_by('year')
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()

    context = {
        'cars': paged_cars,
        'model_search': model_search,
        'fuel_type_search': fuel_type_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request=request, template_name='cars/cars.html', context=context)


def car_detail(request, pk):
    single_car = get_object_or_404(Car, pk=pk)
    context = {
        'single_car': single_car,
    }
    return render(request=request, template_name='cars/car_detail.html', context=context)


def search(request):
    cars = Car.objects.all().order_by('-created_at')

    model_search = Car.objects.values_list('model', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct().order_by('year')
    transmission_search = Car.objects.values_list('transmission', flat=True).distinct()
    fuel_type_search = Car.objects.values_list('fuel_type', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(car_title__icontains=keyword)

    # Filter Search
    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)

    if 'fuel_type' in request.GET:
        fuel_type = request.GET['fuel_type']
        if fuel_type:
            cars = cars.filter(fuel_type__iexact=fuel_type)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)

    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        if transmission:
            cars = cars.filter(transmission__iexact=transmission)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)

    context = {
        'cars': cars,
        'model_search': model_search,
        'body_style_search': body_style_search,
        'year_search': year_search,
        'transmission_search': transmission_search,
        'fuel_type_search': fuel_type_search,
    }
    return render(request=request, template_name='cars/search.html', context=context)
