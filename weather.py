import requests
from bs4 import BeautifulSoup
import datetime


class Weather:

    def __init__(self, location, url):
        self.location = location
        self.url = url
        self.soup = None
        self.temps = None

    def scrape(self):
        r = requests.get(self.url)
        self.soup = BeautifulSoup(r.content, 'html.parser')
        return self.soup

    def find_ten_day_temps(self):
        self.temps = []
        temp = self.soup.find_all('td', class_="temp")
        for i in temp:
            i.find('span', class_="")
            for x in i:
                self.temps.append(x.find('span'))
                for y in x:
                    self.temps.append(y.text)
        del self.temps[0::2]
        return self.temps

    def print_ten_day_temps(self):
        days = []
        date = []
        x = 2
        y = 4
        z = 0
        today = datetime.datetime.now()
        incr_day = datetime.timedelta
        weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

        while z < 11:
            dte = today + incr_day(days=z)
            date.append(dte.strftime("%b %d"))
            weekday = ((today + incr_day(days=z)).weekday())
            days.append(weekdays[weekday])
            z += 1
        print("10 Day Weather Forecast for " + self.location)
        print("Today's weather is " + self.temps[0] + "/" + self.temps[1])
        print("Tomorrow's weather will be " + self.temps[2] + "/" + self.temps[3])
        while x < 11 and y < 22:
            print(days[x] + " " + date[x] + ", the weather will be " + self.temps[y] + "/" + self.temps[y+1])
            x += 1
            y += 2


traverse = Weather("Williamsburg, MI",
                   "https://weather.com/weather/tenday/l/1011eb7ead549e7a528065834339bf6d89bbbfaa6046aad883ce7be11d1f96"
                   "50")

traverse.scrape()
traverse.find_ten_day_temps()
traverse.print_ten_day_temps()
