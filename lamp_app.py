# Meshal Albaiz - lamp_app.py
# Description: takes output of rain probability over the next 12 hours and sets RGB light color
# 11/24/2021

# import RGB light API and rain probability program

from yeelight import Bulb
from  weather_app import rain_probability

IP_address = "XXX.XXX.XX.XX"

# initialize bulb using local IP address of bulb
bulb = Bulb(IP_address)

# get color based on rain probability over the next 12 hours
color = rain_probability()

# set bulb color based on color output
if(color == "blue"): # if probability is over 74%
    bulb.set_hsv(240, 100, 100)
elif(color == "orange"): # if probability is 50% - 74%
    bulb.set_hsv(30, 100, 100)
elif(color == "yellow"): # if probability is 25% - 49%
    bulb.set_hsv(45, 100, 100)
else: # if probability is under 25% then color is green
    bulb.set_hsv(120, 100, 100)
