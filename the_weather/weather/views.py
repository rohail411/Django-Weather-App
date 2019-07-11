from django.shortcuts import render
from .models import City
from .forms import CityForm
import requests

# Create your views here.
def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=748910266f52b09456e835b3841aef67'
    city = 'daska'
    cities = City.objects.all()
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    form = CityForm()
    weather_data = []
    for city in cities:
        r = requests.get(url.format(city)).json()
        city_weather = {
            'city':city,
            'temprature':r['main']['temp'],
            'description':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon']
        }
        weather_data.append(city_weather)

    context = {
        'weather_data':weather_data,
        'form':form
    }
    return render(request,'weather/weather.html',context)