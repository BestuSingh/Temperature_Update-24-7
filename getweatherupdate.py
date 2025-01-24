import requests

City_name = 'Mumbai'
API_KEY = '9364893b893d952f59ea137bd937b013'
url = f'https://api.openweathermap.org/data/2.5/weather?q={City_name}&appid={API_KEY}&units=metric'


response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print('Weather is', data['weather'][0]['description'])
    print('Current Temprature is', data['main']['temp'])
    print('Current Temperature Feels Like is', data['main']['feels_like'])
    print('Humidity is', data['main']['humidity'])