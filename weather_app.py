# Meshal Albaiz - weather_app.py
# Description: produces the highest probability of rain over the next 12 hours
# 11/24/2021

# import requests and json for getting the weather info and parsing it

import requests, json

# API key for using the OpenWeatherMap API
api_key = "XXXXX"

# Latitude and longitude of city
lat = "21.33"
lon = "-158.05"

# URL to request weather information
complete_url = "https://api.openweathermap.org/data/2.5/onecall?lat="+lat+"&lon="+lon+"&exclude=current,minutely,daily,alerts&appid=" + api_key

# request weather info
response = requests.get(complete_url)

# function to return color based on highest probability
def rain_probability():
    weather_info = response.json() # put response in json format
    hourly = weather_info["hourly"] # get hourly weather
    highest_probablity = 0 # start initial highest probability to 0
    for i in range(0, 12): # loop over the next 12 hours
        the_hour = hourly[i] # get info of each hour
        rain_prob = the_hour["pop"] # get the precipitation probability of each hour
        if rain_prob > highest_probablity: # set the highest probability
            highest_probablity = rain_prob

    print("The highest probability of rain in the next 12 hours is " + str(highest_probablity*100) + "%")

    # return color name based on probability
    if highest_probablity >= 0.75:
        return "blue"
    elif highest_probablity >= 0.5:
        return "orange"
    elif highest_probablity >= 0.25:
        return "yellow"
    else:
        return "green"
