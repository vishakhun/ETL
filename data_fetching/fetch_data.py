import requests
import json

def fetch_mars_weather(api_key: str) -> None:
    """
    Fetches Mars weather data from the NASA InSight API and saves it as a JSON file.

    Parameters:
    api_key (str): NASA API key for authentication.

    Returns:
    None
    """
    url = f"https://api.nasa.gov/insight_weather/?api_key={api_key}&feedtype=json&ver=1.0"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        with open('mars_weather.json', 'w') as f:
            json.dump(data, f)
        print("Data fetched and saved successfully.")
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

if __name__ == "__main__":
    API_KEY = "YOUR_API_KEY"  # Replace with your actual API key
    fetch_mars_weather(API_KEY)
