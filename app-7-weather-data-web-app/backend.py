import requests

API_KEY = "f83e9e90b6bc04fe761a6d50715ab2c4"

def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    num_of_values = 8 * forecast_days # 5 day at 3 hour interval forecast data means 24/3 = 8 data points in a day
    filtered_data = filtered_data[:num_of_values]
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3, weather_type="Temperature"))