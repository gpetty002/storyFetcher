import json
import os

def load_raw_data(filename="../data/raw/response.json"):
  os.makedirs(os.path.dirname(filename), exist_ok=True)
  with open(filename, "r") as file:
    return json.load(file)

def filter_relevant_entries(docs):
  filtered = []
  authors_books = []
  for doc in docs:
    description = " ".join(doc.get("description", []))
    if any(keyword in description for keyword in ["Aztec", "Maya", "Inca"]):
      author_title = (doc.get("creator"), doc.get("title"))
      if author_title not in authors_books:
        filtered.append({
          "title": doc.get("title"),
          "creator": doc.get("creator"),
          "description": description,
          "data": doc.get("data"),
          "identifier": doc.get("identifier")
        })
        authors_books.append(author_title)
  return filtered

def save_filtered_data(filtered, filename="../data/processed/filtered_stories.json"):
  with open(filename, "w") as file:
    json.dump(filtered, file, indent=4)