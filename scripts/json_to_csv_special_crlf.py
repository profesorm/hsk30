import json
import csv
import glob

files = glob.glob("*.json")  # all JSON files in the folder

for file in files:

    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)

    records = data["data"]["records"]

    # replace newline characters
    for r in records:
        for k, v in r.items():
            if isinstance(v, str):
                v = v.replace("\n", "<\\n>")
                v = v.replace("\r", "<\\r>")
                r[k] = v


    csv_file = file.replace(".json", ".csv")

    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=records[0].keys())
        writer.writeheader()
        writer.writerows(records)

    print("written:", csv_file)
