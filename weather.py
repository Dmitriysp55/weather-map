import requests
from mapper import degreeToDirectionMapper

city = input('Enter a location: ')
KEY = '2958c38adfca4bfd7f2d30b341168f11'
KEY2 = 'b1d3773306ca860d308f7cb592e017c9'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={KEY2}&units=metric'

print('Updating weather...')
res = requests.get(url)
data = res.json()

if data['cod'] == 200:
    print("Located in: ", data['sys']['country'])
    print("Weather: ", data['weather'][0]['main'])
    print("Temperature: ", data['main']['temp'])
    print("Wind speed: ", data['wind']['speed'], 'Wind direction: ', degreeToDirectionMapper(data['wind']['deg']))
else:
    print(f"Error: code {data['cod']} --> {data['message']}")
# print(data)
