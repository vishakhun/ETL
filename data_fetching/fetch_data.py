import requests
from google.cloud import storage
import json

def fetch_mars_weather(api_key: str) -> dict:
    """Fetch Mars weather data from the NASA API."""
    url = f"https://api.nasa.gov/insight_weather/?api_key={api_key}&feedtype=json&ver=1.0"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

def save_to_gcs(data: dict, bucket_name: str, destination_blob_name: str) -> None:
    """Save fetched data to GCS."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_string(data=json.dumps(data), content_type='application/json')

if __name__ == "__main__":
    API_KEY = "YOUR_API_KEY"  # Replace with your actual NASA API key
    BUCKET_NAME = "your-bucket-name"  # Replace with your GCS bucket name
    FILE_NAME = "mars_weather.json"  # The file name in GCS

    data = fetch_mars_weather(API_KEY)
    save_to_gcs(data, BUCKET_NAME, FILE_NAME)
