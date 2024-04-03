import requests
import tkinter as tk
from tkinter import scrolledtext
import json

# Replace 'your_api_key' with your actual API key
API_KEY = 'your_api_key'
# Replace 'your_city' with your city
CITY = 'your_city'
# API URL with placeholders for the API key and city
URL = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(CITY, API_KEY)

def get_weather():
    response = requests.get(URL)
    if response.status_code == 200:  # Check if request was successful
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        # You can extract more data here as needed
        display_weather(weather, temperature)
    else:
        print("Error fetching weather data")

def display_weather(weather, temperature):
    window = tk.Tk()
    window.title("Weather")
    text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=10)
    text_area.grid(column=0, pady=10, padx=10)
    weather_info = "Weather: {}\nTemperature: {}°C".format(weather, temperature)
    text_area.insert(tk.INSERT, weather_info)
    text_area.configure(state='disabled')
    window.mainloop()

if __name__ == "__main__":
    get_weather()
