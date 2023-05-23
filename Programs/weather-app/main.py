import requests
import pyttsx3
import json
from geopy.geocoders import Nominatim

print("Welcome to Command Line Speak Weather App")
print("-----------------------------------------")
print("NOTE : type 'exit' to sop the app\n")

geolocator = Nominatim(user_agent="MyApp")
engine = pyttsx3.init()

while True:
    city = input("Enter the name of city to get current temperature:  ")
    if city == "exit":
        break
    location = geolocator.geocode(city)
    # print("The latitude of the location is: ", location.latitude)
    # print("The longitude of the location is: ", location.longitude)

    url = f"https://api.open-meteo.com/v1/forecast?latitude={location.latitude}&longitude={location.longitude}&hourly=temperature_2m&current_weather=true"

    response = requests.get(url)
    weather = json.loads(response.text)
    current_temperature = weather["current_weather"]["temperature"]

    engine.say(f"The current temperature in {city} is {current_temperature} degree celsius.")
    engine.runAndWait()