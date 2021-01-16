# importing requests and json
import requests, json, pyowm
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
print(lol.forecast_at_place('New York,USA','daily').forecast)