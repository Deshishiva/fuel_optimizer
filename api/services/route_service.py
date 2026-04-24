import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ORS_API_KEY")

def get_route(start, end):
    try:
        if not API_KEY:
            raise Exception("API Key not found. Check .env file")

        url = "https://api.openrouteservice.org/v2/directions/driving-car"

        headers = {
            'Authorization': API_KEY,
            'Content-Type': 'application/json'
        }

        body = {
            "coordinates": [
                [start["lng"], start["lat"]],
                [end["lng"], end["lat"]]
            ]
        }

        response = requests.post(url, json=body, headers=headers, timeout=10)

        if response.status_code != 200:
            raise Exception(f"API Error: {response.text}")

        data = response.json()

        if "routes" not in data:
            raise Exception(f"Invalid response: {data}")

        distance = data["routes"][0]["summary"]["distance"] / 1609
        geometry = data["routes"][0]["geometry"]

        return distance, geometry

    except Exception as e:
        print("Route Error:", e)
        raise