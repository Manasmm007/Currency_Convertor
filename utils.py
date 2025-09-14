import os
import time
import json
import requests

def get_updates(cache_file='rates.json'):
    # Check if cache exists
    if os.path.exists(cache_file):
        with open(cache_file, 'r') as f:
            try:
                data = json.load(f)
                next_update = data.get('time_next_update_unix', 0)

                if time.time() < next_update:
                    print("Using cached exchange rate data.")
                    return data
            except json.JSONDecodeError:
                pass  # fallback to fetching new data

    # Fetch from API
    print("Fetching new exchange rate data...")
    url = "https://open.er-api.com/v6/latest/INR"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data.get('result') == 'success':
            # Save to cache
            with open(cache_file, 'w') as f:
                json.dump(data, f, indent=2)
            return data

    return None
