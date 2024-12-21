import requests
import internetarchive as ia

text_urls = []

def check_text_availability(identifier):
  url = f"https://archive.org/metadata/{identifier}"
  try:
    response = requests.get(url)
    if response.status_code == 200:
      data = response.json()
      for file in data.get("files", []):
        if file.get("format") == "Text" and file.get("name").endswith(".txt"):
          return f"https://archive.org/download/{identifier}/{file['name']}"
      return None
  except Exception as e:
    print(f"Error checking text for {identifier}: {e}")
    return None
  
def search_filtered_text(filtered_books):
  for book in filtered_books:
    result = check_text_availability(book['identifier'])

    if result != None:
      text_urls.append(result)
  

def fetch_available_books(filtered_books):
  search_filtered_text(filtered_books)

  results = []

  if len(text_urls) == 0:
    return None

  for url in text_urls:
    try:
      response = requests.get(url)
      if response.status_code == 200:
        results.append(response.text)
      else:
        break
    except Exception as e:
      print(f"Error fetching text: {e}")
      return None
    
  
  if len(results) == 0:
    return None
  
  return results