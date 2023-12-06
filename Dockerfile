# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV CSV_FILE /app/csv_data/data.csv
ENV API_KEY=ac25c16a78d45e7c36316f4509c32a71
ENV CITY=Santana
ENV COUNTRY=RO

RUN mkdir "/app/csv_data"
# Run app.py when the container launches
CMD ["python", "app.py"]
