# us-states-mongodb-polygons

This project includes a Python script that reads GeoJSON files from a specified directory (`./us-states` by default) and extracts specific properties like state codes and geometries. The extracted data is then saved to a JSON file.

## Requirements

- Python 3.x
- The directory containing the `.geojson` files must be in the specified path.

## Usage

1. Place your `.geojson` files in the `./us-states` directory.
2. Run the `index.py` script:
3. The processed data will be saved to `./data/us-states.json`.

## Functionality

The `index.py` script performs the following actions:

- Iterates through all the `.geojson` files in the specified directory.
- Opens and reads each file, parsing the GeoJSON content.
- Extracts the state abbreviation and geometry from each file.
- Appends the extracted data to a list.
- Writes the collected data to a JSON file.

## Customization

- You can modify the `STATES_PATH` variable in the `index.py` script to point to a different directory containing your `.geojson` files.
