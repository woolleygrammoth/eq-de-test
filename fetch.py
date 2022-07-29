import requests
from urllib.error import HTTPError
from config import API_KEY, CITY_ID

def fetch_raw_data(CITY_ID: int=CITY_ID, API_KEY: str=API_KEY) -> dict: 
    """
    Use credentials to retrieve raw data
    returns: raw data in json format (response.json())
    """
    url = f'https://api.openweathermap.org/data/2.5/forecast?id={CITY_ID}&units=metric&appid={API_KEY}'
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}') 
    raw = response.json()
    return raw
