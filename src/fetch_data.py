import requests
import json
import os

def fetch_data(query, rows=50, start=0):
  # Fetch and return results
  BASE_URL = "https://archive.org/advancedsearch.php"
  params = {
    "q" : query,
    "fl[]": ["identifier", "title", "creator", "description", "date"],
    "rows": rows,  # Number of results per query
    "output": "json",
    "page": 1,
    "start": start
  }

  response = requests.get(BASE_URL, params=params)

  if response.status_code == 200:
    return response.json()
  else:
    raise Exception(f"Error fetching data: {response.status_code}")

def save_raw_data(data, filename="../data/raw/response.json"):   
  # Save to JSON file
  os.makedirs(os.path.dirname(filename), exist_ok=True)
  with open(filename, "w") as file:
      json.dump(data, file, indent=4)

