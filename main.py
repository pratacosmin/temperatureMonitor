import json
import os
import csv
from flask import Flask, request, jsonify, Response
from dataMonitor import WorkingDetails
from data_processing import CsvToJsonConverter
from flask_basicauth import BasicAuth

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = os.getenv("API_USERNAME", "cosmin")
app.config['BASIC_AUTH_PASSWORD'] = os.getenv("API_PASSWORD", "cosmin19951997")
basic_auth = BasicAuth(app)

@app.route("/updateWorkingStatus", methods=["POST"])
def log_activity():
    data = request.get_json()
    print(data)
    activity = WorkingDetails(duration=data["duration"], date=data["date"], date_time=data["date_time"])
    activity.set_temperature()
    data_writer = CsvToJsonConverter()
    data_writer.json_to_csv(activity.get_log_data())
    return "ok", 200


@app.route('/read_csv', methods=['GET'])
def read_csv():
    try:
        # Replace 'your_file.csv' with the actual path to your CSV file
        csv_file_path = os.getenv("CSV_FILE", "data.csv")

        # Read CSV file
        with open(csv_file_path, 'r') as csv_file:
            csv_data = csv_file.read()

        # Set response headers for CSV
        headers = {
            'Content-Type': 'text/csv',
            'Content-Disposition': f'attachment; filename={csv_file_path}'
        }

        # Return CSV data as a response
        return Response(csv_data, headers=headers, status=200)
    except Exception as e:
        # Handle any exceptions that might occur
        return jsonify({'error': str(e)}), 500


@app.route('/')
def health_check():
    return 'OK', 200

if __name__ == '__main__':
    app.run(debug=True, port=9090)