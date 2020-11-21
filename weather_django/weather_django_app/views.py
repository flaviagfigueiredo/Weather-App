from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import JsonResponse, HttpResponse
import requests, json
from datetime import datetime
from weather_django_app.info import getWeatherData, convertTime


URL_API = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=88e7f21e91060a4d599e8efa2141e943'

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def weather(request):
    starter_cities = ['Porto','Lisboa']
    data = []
    for city in starter_cities:
        data.append(getWeatherData(city))

    params = { 'data' : data }  
    return render(request, 'weather.html', params)

def data(request):
    if request.method == 'GET':
        city = request.GET.get('name', None)
        data = getWeatherData(city)
        context = {'data' : data}
        return JsonResponse(context, status=200)
    return JsonResponse({'success': False, 'error': 'Connection refused'}, status=400)

