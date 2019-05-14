import requests
from bs4 import BeautifulSoup


class Weather:

    def __init__(self, zipcode):
        self.location_name = None
        self.zipcode = zipcode
        self.soup = None
        self.todays_temp = []
        self.today_feel_like = None
        self.today_description = None
        self.todays_conditions = []
        self.today_precip = None
        self.today_short_description = None
        self.today_sunrise = None
        self.today_sunset = None
        self.request_times = None

    def scrape(self):
        r = requests.get("https://weather.com/weather/today/l/" + self.zipcode,
                         headers={'Cache-Control': 'no-cache'})
        self.soup = BeautifulSoup(r.content, 'html.parser')

    def find_todays_weather(self):
        self.location_name = self.soup.find('h1', class_='today_nowcard-location').text
        self.today_feel_like = self.soup.find('span', class_='deg-feels').text
        self.today_description = self.soup.find('div', class_='today_nowcard-phrase').text
        self.today_precip = self.soup.find('span', class_='precip-val').text
        self.today_short_description = self.soup.find('span', class_='today-wx-descrip').text
        self.today_sunrise = self.soup.find('span', id='dp0-details-sunrise').text
        self.today_sunset = self.soup.find('span', id='dp0-details-sunset').text
        self.request_times = self.soup.find('p', class_='today_nowcard-timestamp').text
        today_condition = self.soup.find('div', class_='today_nowcard-sidecar')
        for x in today_condition.find_all('td'):
            self.todays_conditions.append(x.text)
        today_temp_high = self.soup.find('div', class_='today_nowcard-temp')
        self.todays_temp.append(today_temp_high.text)
        today_temp_low = self.soup.find('span', class_='deg-hilo-nowcard')
        self.todays_temp.append(today_temp_low.next_sibling.next_sibling.next_sibling.text)

    def locations_name(self):
        return self.location_name

    def todays_high(self):
        return self.todays_temp[0]

    def todays_low(self):
        return self.todays_temp[1]

    def todays_feels_like(self):
        return self.today_feel_like

    def todays_wind(self):
        return self.todays_conditions[0]

    def todays_humidity(self):
        return self.todays_conditions[1]

    def todays_dew_point(self):
        return self.todays_conditions[2]

    def todays_pressure(self):
        return self.todays_conditions[3]

    def todays_visibility(self):
        return self.todays_conditions[4]

    def todays_description(self):
        return self.today_description

    def todays_short_description(self):
        return self.today_short_description

    def todays_precipitation(self):
        return self.today_precip

    def todays_sunrise(self):
        return self.today_sunrise

    def todays_sunset(self):
        return self.today_sunset

    def request_time(self):
        return self.request_times
