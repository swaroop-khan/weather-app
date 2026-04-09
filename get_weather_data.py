import requests

city_name=input("Enter city name: ")
from dotenv import load_dotenv
import os

load_dotenv()
API_Key = os.getenv('API_KEY')
url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}&units=metric'

response=requests.get(url)

if response.status_code==200:
    data=response.json()
    weather_description=data['weather'][0]['description']
    if 'rain' in weather_description:
        icon = '🌧️'
    elif 'cloud' in weather_description:
        icon = '☁️'
    elif 'clear' in weather_description:
        icon = '☀️'
    elif 'snow' in weather_description:
        icon = '❄️'
    else:
        icon = '🌡️'
    print(f"City 📍: {data['name']}")
    print(f"Weather is: {data['weather'][0]['description']}")
    print(f"Current Temperature 🌡️ : {data['main']['temp']}°C")
    print(f"Humidity is: {data['main']['humidity']}%")
else:
    print(f"City not found💭; Status code: {response.status_code}")