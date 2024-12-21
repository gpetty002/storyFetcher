import json

# Input and output file paths
input_file = "fine_tuned_stories.json"
output_file = "test.jsonl"

# Read the JSON file
with open(input_file, "r") as infile:
    data = json.load(infile)

# Write to a JSONL file
with open(output_file, "w") as outfile:
    for obj in data:
        outfile.write(json.dumps(obj) + "\n")

print(f"Converted {input_file} to {output_file} in JSONL format.")
