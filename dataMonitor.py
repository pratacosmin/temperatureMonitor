import os

import requests as requests


class WorkingDetails():
    def __init__(self, date_time, date,  duration):
        self.date_time = date_time
        self.date = date
        self.duration = duration
        self.city = os.getenv("CITY")
        self.country = os.getenv("COUNTRY")
        self.api_key = os.getenv("API_KEY")

    def get_log_data(self):
        data = self.__dict__
        data.pop("api_key")
        return data

    def set_temperature(self):
        # OpenWeatherMap API endpoint for current weather
        api_url = "http://api.openweathermap.org/data/2.5/weather"

        # Parameters for the API request
        params = {
            'q': f'{self.city},{self.country}',
            'appid': self.api_key,
            'units': 'metric'  # Use 'imperial' for Fahrenheit
        }

        # Make the API request
        response = requests.get(api_url, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            weather_data = response.json()

            # Extract temperature from the response
            temperature = weather_data['main']['temp']

            self.temperature = temperature
        else:
            # Print an error message if the request was not successful
            print(f"Error: Unable to fetch weather data. Status code: {response.status_code}")
            self.temperature = None


