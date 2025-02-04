import requests
import csv
from datetime import datetime
from constaints import API_KEY

LATITUDE = 33.8688 #sydney
LONGITUDE = 151.2093 #sydney

def get_weather_data(lat, lon, api_key):
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(weather_url)
    
    if response.status_code == 200:
        data = response.json()
        temp_c = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        location_name = data.get("name", "Unknown") or f"Lat:{lat}, Lon:{lon}"
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Fetch air quality data
        air_quality = get_air_quality(lat, lon, api_key)
        
        return [location_name, timestamp, temp_c, air_quality, humidity, wind_speed]
    
    print(f"Failed to get weather data: {response.status_code}")
    return None

def get_air_quality(lat, lon, api_key):
    aqi_url = f"https://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(aqi_url)
    
    if response.status_code == 200:
        data = response.json()
        air_quality_index = data["list"][0]["main"]["aqi"]
        return air_quality_index  # AQI values range from 1 (Good) to 5 (Very Poor)
    
    print("Failed to fetch air quality data.")
    return "N/A"

def save_to_csv(data, filename="s3://rahul-weather-airflow-bucket/weather_data.csv"):
    headers = ["Location", "Time", "Temperature (C)", "Air Quality", "Humidity", "Wind Speed"]
    try:
        with open(filename, mode="a", newline="") as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(headers)  # Write headers only if the file is empty
            writer.writerow(data)
        print("Data saved successfully.")
    except Exception as e:
        print(f"Error saving data: {e}")

def runWeather():
    weather_data = get_weather_data(LATITUDE, LONGITUDE, API_KEY)
    if weather_data:
        save_to_csv(weather_data)