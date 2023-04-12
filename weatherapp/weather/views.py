import os
import requests
from django.shortcuts import render

from weather.forms import CityForm
from weather.models import City


def index(request):
    appid = os.getenv('appid')
    url = (
            'https://api.openweathermap.org/data/2.5/weather'
            '?q={}&units=metric&appid=' + appid
    )

    form = CityForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CityForm()

    cities = City.objects.all()
    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'feels_like': res['main']['feels_like'],
            'icon': res['weather'][-1]['icon'],
        }
        all_cities.append(city_info)
    return render(
        request, 'weather/index.html', {'all_info': all_cities, 'form': form},
    )
