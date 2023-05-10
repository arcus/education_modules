FROM python:3.9-slim-buster

# set working directory in container
# WORKDIR non needed right now because requirments.txt is in the same directory as Dockerfile

# Copy and install packages
COPY requirements.txt /
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

# Copy the whole directory into the Docker container
COPY . . /

# Run locally
CMD gunicorn --bind 0.0.0.0:8050 app:server
