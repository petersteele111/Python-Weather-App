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

**Ten Day Forecast**  
```
# Create the object
sault.Weather('Sault Ste. Marie', '49783') 

# Gets the 10 day forecast. See source code for forecast.type[] list
# Use index of list item for the type of forecast you want
sault.scrape(3)

# Finds the temps from the website
sault.find_ten_day_temps() 

# Dynamically builds the output to the terminal based on the parsed data
sault.print_ten_day_temps() 
```
**Expected Output**
```
10 Day Weather Forecast for Sault Ste. Marie
Today's weather is --/41°
Tomorrow's weather will be 61°/39°
Wednesday May 15, the weather will be 69°/46°
Thursday May 16, the weather will be 61°/39°
Friday May 17, the weather will be 58°/43°
Saturday May 18, the weather will be 57°/42°
Sunday May 19, the weather will be 58°/44°
Monday May 20, the weather will be 58°/47°
Tuesday May 21, the weather will be 58°/44°
Wednesday May 22, the weather will be 61°/45°
Thursday May 23, the weather will be 61°/45°
```

**Today's current temp and projected low**
```
sault.Weather('Sault Ste. Marie', '49783')
sault.scrape(0)
sault.find_todays_temp()
sault.print_todays_temp()
```
**Expected Output**
```
The current temperature is 45° and the low for today will be 41°
```
So basically I have split this up into several different methods. The reason behind this so far, is that I want as much modularity as possible for now regarding finding the temps, formatting and printing the temps, scraping the site for the temps, etc. 
This may change in the future as I update the program and add more features. I will reflect these changes here in the README as necessary.

# Conclusion
Thank you all for checking out my repo and app. This is very much a work in progress and new features and 
restructuring are done daily. As mentioned above, if you have any questions, comments, or concerns, please don't 
hesitate to contact me at info@pbsteele.com and I will be more than happy to read and reply to those messages. 

**This is a work in progress. The source code here is released under the GNUv3 License. Thank you**
