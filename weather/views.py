from django.shortcuts import render,redirect
import urllib.request
import json
from django.contrib import messages


def home(request):
    if request.method == 'POST':
        city = request.POST['city']
        city = city.replace(' ', '+')
        try:
            source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&appid=b4c651fb28a6b62cb5a993142c60898c').read()
        except:
            messages.warning(request, "ERROR MESSAGE: COUNTRY IS INCORRECT")
            return redirect('/')
        json_data = json.loads(source)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon'])+','+str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp'])+' °C',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
            "main": str(json_data['weather'][0]['main']),
            "description": str(json_data['weather'][0]['description']),
            "icon": str(json_data['weather'][0]['icon']),
        }
        print(data)
    else:
        data = {}

    return render(request, 'home.html', {'result': data})
