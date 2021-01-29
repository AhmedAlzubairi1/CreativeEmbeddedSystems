#importing requests and json
import requests, json, pyowm
from datetime import date
# base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = "New York"
API_KEY = "1af163a7e26daeeb2a085b21b7909998"
# upadting the URL
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
# HTTP request
response = requests.get(URL)
# checking the status code of the request
if response.status_code == 200:
   # getting data in the json format
   data = response.json()
   # getting the main dict block
   main = data['main']
   # getting temperature
   temperature = main['temp']
   # getting the humidity
   humidity = main['humidity']
   # getting the pressure
   pressure = main['pressure']
   # weather report
   report = data['weather']
   print(f"{CITY:-^30}")
   print(f"Temperature: {temperature}")
   print(f"Humidity: {humidity}")
   print(f"Pressure: {pressure}")
   print(f"Weather Report: {report[0]['description']}")
   #print(data)
else:
   # showing the error message
   print("Error in the HTTP request")
owm=pyowm.OWM(API_KEY)
lol=owm.weather_manager()
obs=lol.weather_at_place('New York,USA')
print(dir(obs.weather))
print(121)
print(obs.weather.status)
print(obs.weather.temperature('fahrenheit'))
print(obs.weather.rain)

#print(lol.forecast_at_place('New York,USA','daily'))
#one_call=lol.one_call()
print('22222')
print(dir(owm))
mgr = owm.weather_manager()
one_call = mgr.one_call(lat=40.7128, lon=74.0060)
print(dir(one_call))
print(one_call.forecast_daily)

print('chec'*10)
print(dir(one_call.forecast_hourly[0]))
print(one_call.forecast_hourly[0].status)
print(dir(one_call.forecast_hourly[0].reference_time))
word=str(one_call.forecast_hourly[0].reference_time)
word=word[word.find('reference_time='):]
word=word[word.find('='):]
day=word[9:11]
print(day)

current_day_weather=str(one_call.forecast_hourly[0].reference_time)
today_date=current_day_weather[current_day_weather.find('reference_time='):]
today_date=today_date[today_date.find('='):][9:11]
print(today_date)
isRain=False or 'rain' in one_call.forecast_hourly[0].status.lower()
print(isRain)
print(one_call.forecast_hourly[0].status.lower())
for hour in one_call.forecast_hourly:
    if isRain:
        break
    this_date_weather=str(hour.reference_time)
    this_date=this_date_weather[this_date_weather.find('reference_time='):]
    this_date=this_date[this_date.find('='):][9:11]
    if this_date != today_date:
        break
    if 'rain' in hour.status.lower():
        isRain=True
        break
print('ssss' + str(date.today().day))