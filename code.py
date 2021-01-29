import requests, json, pyowm
from datetime import date
import board
import neopixel
import time
time.sleep(40)
pixel_pin = board.D21

# The number of NeoPixels
num_pixels = 8
 
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.RGB
 
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)
def blink():
    global pixels
    
    #GRB
    pixels.fill((0,0,255))
    pixels.show()
    time.sleep(0.1)
    
    pixels.fill((0,128,128))
    pixels.show()
    time.sleep(0.1)

    

def normal():
    global pixels
    pixels.fill((255,0,0))
    pixels.show()
    time.sleep(1)
    pixels.show()

def will_rain():
    # base URL
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = "New York"
    API_KEY = "1af163a7e26daeeb2a085b21b7909998"
    # upadting the URL
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    owm=pyowm.OWM(API_KEY)
    mgr = owm.weather_manager()
    one_call = mgr.one_call(lat=40.7128, lon=74.0060)
    current_day_weather=str(one_call.forecast_hourly[0].reference_time)
    today_date=current_day_weather[current_day_weather.find('reference_time='):]
    today_date=today_date[today_date.find('='):][9:11]
    isRain=False or 'rain' in one_call.forecast_hourly[0].status.lower()
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
    return  not isRain

global_day=str(date.today().day)

in_diff_day=True
rain=False
#while true should be here
while True:

    if in_diff_day:
        if will_rain():
            rain=True
        else:
            rain=False
    if rain:
        blink()
    else:
        normal()
    if str(date.today().day) != global_day:
        in_diff_day=True
    else:
        in_diff_day=False
    if in_diff_day:
        global_day=str(date.today().day)
