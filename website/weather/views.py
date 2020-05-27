from django.shortcuts import render
from django.db.models import Q
from django.contrib import messages
import requests
from .models import City

def weather_view(request):
    cities = City.objects.all()
    final_data = []
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=c117c95d4369947a04da6a8886dbbbdb'
    for city in cities:
        city_weather = requests.get(url.format(city.name)).json()
        description = city_weather['weather'][0]['description']
        temperature = city_weather['main']['temp']-273
        icon = city_weather['weather'][0]['icon']
        data = {'city':city, 'temperature':temperature, 'description':description, 'icon':icon}
        final_data.append(data)
    return render(request, 'home.html', {'final_data':final_data})

def search(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=c117c95d4369947a04da6a8886dbbbdb'
    final_data = []
    if request.method=='POST':
        q = request.POST['q']
        if q:
            match = City.objects.filter(Q(name__icontains=q))
            if match:
                city = match[0]
                city_weather = requests.get(url.format(city)).json()
                description = city_weather['weather'][0]['description']
                temperature = city_weather['main']['temp']-273
                icon = city_weather['weather'][0]['icon']
                data = {'city':city, 'temperature':temperature, 'description':description, 'icon':icon}

                final_data.append(data)
                return render(request, 'home.html', {'queries':final_data})
    return render(request, 'home.html')
