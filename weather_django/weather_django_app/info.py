import requests, json
from datetime import datetime

URL_API = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=88e7f21e91060a4d599e8efa2141e943'

def getWeatherData(name):
    r = requests.get(URL_API.format(name)).json()
    city_weather = {
    'city' : name,
    'temperature' : round((r['main']['temp'] - 32) * 5/9,1),
    'sunset': convertTime(r['sys']['sunset']),
    'sunrise': convertTime(r['sys']['sunrise']),
    'description' : r['weather'][0]['description'],
    'icon' : r['weather'][0]['id'],
    }

    return city_weather

def convertTime(ts):
    return (datetime.utcfromtimestamp(ts).strftime('%H:%M'))
