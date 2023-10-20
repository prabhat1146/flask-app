# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Create and set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY . /app
RUN pip install -r requirements.txt

# Expose port 5000 for the Flask app
EXPOSE 5000

# Define the command to run your application
CMD python ./application.py
