# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app
COPY src/machines_.json /app/src/machines.json 

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run app.py when the container launches
WORKDIR /app/src
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${LISTEN_PORT} main:app"]