import requests
from bs4 import BeautifulSoup
import datetime


class Weather:

    def __init__(self, location_name, zipcode):
        self.location_name = location_name
        self.zipcode = zipcode
        self.soup = None
        self.todays_temp = None
        self.ten_day_temps = None
        self.forecast_type = ['today', 'hourbyhour', '5day', 'tenday', 'weekend', 'monthly']

    def scrape(self, report):
        r = requests.get("https://weather.com/weather/" + self.forecast_type[report] + "/l/" + self.zipcode)
        self.soup = BeautifulSoup(r.content, 'html.parser')
        return self.soup

    def find_todays_temp(self):
        self.todays_temp = []
        today_temp_high = self.soup.find('div', class_='today_nowcard-temp')
        self.todays_temp.append(today_temp_high.text)
        today_temp_low = self.soup.find('span', class_='deg-hilo-nowcard')
        self.todays_temp.append(today_temp_low.next_sibling.next_sibling.next_sibling.text)
        return self.todays_temp

    def find_ten_day_temps(self):
        self.ten_day_temps = []
        ten_day_temp = self.soup.find_all('td', class_="temp")
        for i in ten_day_temp:
            i.find('span', class_="")
            for x in i:
                self.ten_day_temps.append(x.find('span'))
                for y in x:
                    self.ten_day_temps.append(y.text)
        del self.ten_day_temps[0::2]
        return self.ten_day_temps

    def print_todays_temp(self):
        print("The current temperature is " + self.todays_temp[0] + " and the low for today will be " +
              self.todays_temp[1])

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
        print("10 Day Weather Forecast for " + self.location_name)
        print("Today's weather is " + self.ten_day_temps[0] + "/" + self.ten_day_temps[1])
        print("Tomorrow's weather will be " + self.ten_day_temps[2] + "/" + self.ten_day_temps[3])
        while x < 11 and y < 22:
            print(days[x] + " " + date[x] + ", the weather will be " + self.ten_day_temps[y] + "/" +
                  self.ten_day_temps[y+1])
            x += 1
            y += 2


# home = Weather("Williamsburg, MI", "49690")
# home.scrape(3)
# home.find_ten_day_temps()
# home.print_ten_day_temps()
#
sault = Weather('Sault Ste. Marie', '49783')
sault.scrape(0)
sault.find_todays_temp()
sault.print_todays_temp()