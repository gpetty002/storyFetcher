# import schedule
# import time
from fetch_data import fetch_data, save_raw_data
from process_data import load_raw_data, filter_relevant_entries, save_filtered_data
from classify_text import classify_text
from check_text_availability import fetch_available_books
import os
import json

classified_books = []

def fetch_and_process():
  raw_data = fetch_data(query="Aztec OR Maya OR Inca", rows=50)
  save_raw_data(raw_data)
  docs = load_raw_data()["response"]["docs"]
  filtered = filter_relevant_entries(docs)
  classified = classify_text(filtered)
  save_filtered_data(classified)

def load_filtered_data(filename):
  os.makedirs(os.path.dirname(filename), exist_ok=True)
  with open(filename, "r") as file:
    return json.load(file)

def search_data_for_stories():
  classified_books = load_filtered_data("../data/processed/filtered_stories.json")
  print(fetch_available_books(classified_books))

# fetch_and_process()
search_data_for_stories()
# Schedule tasks
# schedule.every(14).days.do(fetch_and_process)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
