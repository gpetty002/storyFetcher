from openai import OpenAI
import sys
import json
sys.path.append('../')
import config

# Initialize the OpenAI client with your API key
client = OpenAI(api_key=config.api_key)

def classify_text(filtered_books, model="gpt-4"):
  classified_books = []

  for book in filtered_books:
    description = book.get("description", "")
    if not description:
      continue
    
    # Prepare messages for classification
    messages = [
      {"role": "system", "content": "You are an expert in classifying books as 'non-fiction' or 'fiction' based on their title and description."},
      {"role": "user", "content": f"Classify this book:\nAuthor: {book['creator']}\nTitle: {book['title']}\nDescription: {description}\nClassification:"}
    ]

    try:
      # Call the OpenAI chat completions API
      response = client.chat.completions.create(
          model=model,
          messages=messages
      )

      # Extract the classification result
      # classification = response['choices'][0]['message']['content'].strip().lower()
      classification = response.choices[0].message.content.strip().lower()
      book["classification"] = classification

      # Append only non-fiction books
      if classification == "non-fiction":
        classified_books.append(book)

    except Exception as e:
      print(f"Error classifying book {book['title']}: {e}")

  return classified_books


def process_classifications(filtered_data, output_file="data/processed/classified_stories.json"):
    classified_books = classify_text(filtered_data)
    
    # Save the classified books to a JSON file
    with open(output_file, "w") as file:
        json.dump(classified_books, file, indent=4)

    print(f"Classified data saved to {output_file}")
