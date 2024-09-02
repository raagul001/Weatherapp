from django.shortcuts import render, redirect, get_object_or_404
from .forms import world
from .models import city
import requests
from django.contrib import messages

# Create your views here.
def home(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={},&appid=4c16c83c4e1be6129a4b707303b95af3&units=metric'

    if request.method == "POST":
        form = world(request.POST)
        if form.is_valid():
            NCity = form.cleaned_data['name']
            CCity = city.objects.filter(name=NCity).count()
            if CCity == 0:
                res = requests.get(url.format(NCity)).json()
                if res['cod'] == 200:
                    form.save()
                    messages.success(request, f"{NCity} Added Successfully...!!!")
                else:
                    messages.error(request, "City Does Not Exist...!!!")
            else:
                messages.error(request, "City Already Exists...!!!")

    d = world()
    my_data = city.objects.all()
    data = []

    for i in my_data:
        res = requests.get(url.format(i.name)).json()
        weather = {
            'city': res['name'],
            'temperature': res['main']['temp'],
            'description': res['weather'][0]['description'],
            'country': res['sys']['country'],
            'icon': res['weather'][0]['icon'],
        }
        data.append(weather)
    context = {'data': data, 'hello': d}
    return render(request, 'Weatherapp.html', context) 

def delete(request, CName):
    CName = CName.strip()  # Remove any leading or trailing whitespace
    city_instance = get_object_or_404(city, name__iexact=CName)  # Case-insensitive match
    city_instance.delete()
    messages.success(request, f"{CName} Removed Successfully...!!!")
    return redirect('home')