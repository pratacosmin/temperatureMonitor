import csv
import json
import os


class CsvToJsonConverter:
    def __init__(self):
        self.csv_file_path = os.getenv("CSV_FILE", "data.csv")

    def read_csv(self):
        data = []
        with open(self.csv_file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)
        return data

    def json_to_csv(self, json_data):
        # Assuming that the JSON data is a list of dictionaries


        # Extract headers from the first dictionary in the list
        headers = json_data.keys()

        # Check if the CSV file exists
        file_exists = os.path.exists(self.csv_file_path)

        # Write data to CSV file
        with open(self.csv_file_path, 'a', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=headers)

            # If the file is empty, write the header
            if not file_exists:
                csv_writer.writeheader()

            # Write rows
            csv_writer.writerow(json_data)
        return True
