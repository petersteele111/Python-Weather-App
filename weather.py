import requests
from bs4 import BeautifulSoup
import datetime

class Scraper:


    def __init__(self, location):
        self.location = location

    def get_tenDayTemps(self):
        r = requests.get(self.location)
        soup = BeautifulSoup(r.content, 'html.parser')
        temps = []

        temp = soup.find_all('td', class_="temp")
        # Temp is now a Result Object
        for i in temp:
            i.find('span', class_="")
            for x in i:
                temps.append(x.contents)
                for y in x:
                    temps.append(y.text)
        days = []
        weekdays = ("Monday's", "Tuesday's", "Wednesday's", "Thursday's", "Friday's", "Saturday's", "Sunday's")

        z = 0
        while z < 11:
            weekday = ((datetime.datetime.now() + datetime.timedelta(days=z)).weekday())
            days.append(weekdays[weekday])
            z += 1

        print("10 Day Weather Forecast")
        print("Today's weather is " + temps[1] + "/" + temps[3])
        print("Tomorrow's weather is " + temps[5] + "/" + temps[7])
        print(days[2] + " weather is " + temps[9] + "/" + temps[11])
        print(days[3] + " weather is " + temps[13] + "/" + temps[15])
        print(days[4] + " weather is " + temps[17] + "/" + temps[19])
        print(days[5] + " weather is " + temps[21] + "/" + temps[23])
        print(days[6] + " weather is " + temps[25] + "/" + temps[27])
        print(days[7] + " weather is " + temps[29] + "/" + temps[31])
        print(days[8] + " weather is " + temps[33] + "/" + temps[35])
        print(days[9] + " weather is " + temps[37] + "/" + temps[39])
        print(days[10] + " weather is " + temps[41] + "/" + temps[43])


traverse = Scraper("https://weather.com/weather/tenday/l/1011eb7ead549e7a528065834339bf6d89bbbfaa6046aad883ce7be11d1f9650")
orlando = Scraper('https://weather.com/weather/tenday/l/bdcad7b003356cef4a2a80034d7f23f4f42464c4341a02051f41860acc458a39')
traverse.get_tenDayTemps()
orlando.get_tenDayTemps()
