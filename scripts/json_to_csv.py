import json
import csv
import glob

files = glob.glob("*.json")  # all JSON files in the folder

for file in files:

    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)

    records = data["data"]["records"]

    csv_file = file.replace(".json", ".csv")

    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=records[0].keys())
        writer.writeheader()
        writer.writerows(records)

    print("written:", csv_file)