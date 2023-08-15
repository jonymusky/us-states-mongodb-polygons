import os
import json

# Path to the folder containing the .geojson files
path = "./us-states"

# List to store the extracted data
data = []

# Iterate through all files in the folder
for filename in os.listdir(path):
    if filename.endswith(".geojson"):
        with open(os.path.join(path, filename), "r") as file:
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

# Write the data to a JSON file
with open("./data/us-states.json", "w") as jsonfile:
    json.dump(data, jsonfile)