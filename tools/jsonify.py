import json

with open("stories.json", "r") as storiesFile:
  data = json.load(storiesFile)

length = len(data)

formatted_data = []

for obj in data:
  formatted_data.append(
    {
      "messages": [
      {
        "role": "system",
        "content": "This is a factual model that provides stories about African and African American, Armenian, Arab, Filipino, Mexican and Latin American, Indian, Vietnamese, Indonesian, Indigenous peoples of New Zealand, Thai cultures."
      },
      {
        "role": "user",
        "content": "provide details in JSON format"
      },
      {
        "role": "assistant",
        "content": json.dumps(obj)
      }
    ]
    }
  )

with open("fine_tuned_stories.json", "w") as file:
  json.dump(formatted_data, file, indent=4)

print("done printing")