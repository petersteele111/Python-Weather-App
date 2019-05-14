# Python Weather App - Peter Steele
This is a hobby project of mine to create a python program that can scrape a weather site and output the current weather, 10 day forecasts, etc. I realize I could simply just go to the websites for this information but where is the fun in that? 

My main goals with this project are to create a class that handles the logic and scraping, while a GUI interface that sits on the desktop queries the proper information and displays it for you. Again, nothing unique here, but I am not going off any other projects similar to this, and I am writing this from the ground up to help myself learn and gain more experience with Python. 

Hopefully you all find this project fun and interesting and can make it something even greater! I'm uploading the 
code under GNUv3 so have at it. If you have any questions or suggestions for a different route I might take then 
please message me at info@pbsteele.com.

# Installation
To install this program, it is rather simple. You will need two modules for python and that's it! I use the requests and BeautifulSoup modules to get the html and parse it for the weather data needed. 

**1.)** To install requests simply run the command:
```pip install requests```

**2.)** To install BeautifulSoup simply run the command:
```pip install bs4```

**3.)** Lastly, download or clone this repo and use the class in any project you might be working on currently. You can also play around with it and just import the class into a blank python file and create as many objects as you want and run the code to output the desired weather. I will be working on a GUI later on that will simplify this even further. 

# Example's
Here I will provide and example of how to curently use the program to get weather information. I only have temps included as of now, but will be working on more relevant information as I flesh this app out. 

**Today's Weather**
```
sault = Weather('49783')
sault.scrape()
sault.find_todays_weather()
print(sault.location_name)
print(sault.todays_high())
print(sault.todays_low())
print(sault.todays_feels_like())
print(sault.todays_wind())
print(sault.todays_description())
print(sault.todays_dew_point())
print(sault.todays_humidity())
print(sault.todays_pressure())
print(sault.todays_visibility())
print(sault.todays_precipitation())
print(sault.todays_short_description())
print(sault.todays_sunrise())
print(sault.todays_sunset())
print(sault.request_time())
```
**Expected Output**
```
Sault Ste Marie, MI # Location Name
39° # Todays High
36° # Todays Low
39° # Todays Feels Like Temp
Calm # Todays Wind
Fair # Todays Desctiption
31° # Todays Dew Point
72% # Todays Humidity
29.93 in # Todays Barometric Pressure
10.0 mi # Todays Visibility
0% # Todays Precipitation Chances
Clear skies. Low 36F. Winds light and variable. # Todays Short Description
6:06 am # Todays Sunrise
9:01 pm # Todays Sunset
as of 3:02 am EDT # Time that website was scraped
```
So basically I have split this up into several different methods. The reason behind this so far, is that I want as much modularity as possible for now regarding finding the temps, formatting and printing the temps, scraping the site for the temps, etc. 
This may change in the future as I update the program and add more features. I will reflect these changes here in the README as necessary.

# Conclusion
Thank you all for checking out my repo and app. This is very much a work in progress and new features and 
restructuring are done daily. As mentioned above, if you have any questions, comments, or concerns, please don't 
hesitate to contact me at info@pbsteele.com and I will be more than happy to read and reply to those messages. 

**This is a work in progress. The source code here is released under the GNUv3 License. Thank you**
