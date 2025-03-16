# Use the official Python image from the Docker Hub
FROM python:3.12-slim

RUN apt-get update && apt-get install -y git

# Where to install virtual environment. Also put this into devcontainer.json PATH
RUN python3 -m venv /opt/myenv
RUN /opt/myenv/bin/pip install --upgrade pip
