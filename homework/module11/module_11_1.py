import requests
from matplotlib import pyplot as plt
import pandas as pd

# получаем координаты Москвы (requests)
city='Moscow' # replace any city of country
result_city = requests.get(url='https://geocoding-api.open-meteo.com/v1/search?name=' + city)
location = result_city.json()
longitude=str(location['results'][0]['longitude'])
latitude=str(location['results'][0]['latitude'])
# print(longitude)
# print(latitude)

# получаем погоду в Москве (requests)
result_weather = requests.get(url='https://api.open-meteo.com/v1/forecast?latitude=' + latitude + '&longitude=' + longitude + '&hourly=temperature_2m&daily=temperature_2m_max,temperature_2m_min&timezone=auto&forecast_days=7')
data = result_weather.json()

# форматируем время и дату (pandas)
times = data['hourly']['time']
dates = pd.to_datetime(times, format='%Y-%m-%dT%H:%M')

values = data['hourly']['temperature_2m']

# отрисовываем графику (matplotlib)
plt.plot(dates.to_list(), values)
plt.title(city + " temperature ")
plt.xlabel("hourly")
plt.ylabel("temperature")
plt.show()
