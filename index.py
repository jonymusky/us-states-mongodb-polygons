"""Module providingFunction printing python version."""
import os
import json

# Path to the folder containing the .geojson files
STATES_PATH = "./us-states"

# List to store the extracted data
data = []

# Iterate through all files in the folder
for filename in os.listdir(STATES_PATH):
    if filename.endswith(".geojson"):
        # Correctly joining the path and specifying the encoding
        with open(os.path.join(STATES_PATH, filename), "r", encoding="utf-8") as file:
            # Read and parse the .geojson file
            geojson = json.load(file)

            # Extract the properties you need
            state_code = geojson["properties"]["abbreviation"]
            geometry = geojson["geometry"]

            # Add the extracted data to the list
            data.append({
                "_id": state_code,
                "geometry": geometry
            })

# Write the data to a JSON file (with specified encoding)
with open("./data/us-states.json", "w", encoding="utf-8") as jsonfile:
    json.dump(data, jsonfile)
    