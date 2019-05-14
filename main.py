import weather

location_name = input("Please enter the locations name >>> ")
location_zipcode = input("Please enter the locations zipcode >>> ")
forecast_type = int(input("Please enter the type of forecast you would like? 0 = Current | 1 = Hour by Hour | 2 = 5 "
                          "Day | 3 = 10 Day | 4 = Weekend | 5 = Monthly >>> "
                          ">>> "))

location_name = weather.Weather(location_name, location_zipcode)
location_name.scrape(forecast_type)
if forecast_type == 0:
    location_name.find_todays_temp()
    location_name.print_todays_temp()
elif forecast_type == 1:
    pass
elif forecast_type == 2:
    pass
elif forecast_type == 3:
    location_name.find_ten_day_temps()
    location_name.print_ten_day_temps()
elif forecast_type == 4:
    pass
elif forecast_type == 5:
    pass
else:
    print("I am sorry, but you input an invalid option. Please try again.")
