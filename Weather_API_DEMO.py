import requests
from bs4 import BeautifulSoup
from weather import Weather

williamsburg = Weather('49690')
williamsburg.scrape()
williamsburg.find_todays_conditions()
print("Location Name:", williamsburg.locations_name())
print("Today's high:", williamsburg.todays_high())
print("Today's Low:", williamsburg.todays_low())
print("Feels Like:", williamsburg.todays_feels_like())
print("Today's Wind:", williamsburg.todays_wind())
print("Today's Description:", williamsburg.todays_description())
print("Today's Dew Point:", williamsburg.todays_dew_point())
print("Today's Humidity:", williamsburg.todays_humidity())
print("Today's Pressure:", williamsburg.todays_pressure())
print("Today's Visibility:", williamsburg.todays_visibility())
print("Today's precipitation:", williamsburg.todays_precipitation())
print("Today's Short Description:", williamsburg.todays_short_description())
print("Today's Sunrise:", williamsburg.todays_sunrise())
print("Today's Sunset:", williamsburg.todays_sunset())
print("Valid", williamsburg.request_time())