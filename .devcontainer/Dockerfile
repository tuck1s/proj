# Use the official Python image from the Docker Hub
FROM python:3.12-slim

RUN apt-get update && apt-get install -y git

# Create a non-root user for python pip
RUN useradd -ms /bin/bash vscode

# Set the environment variable PYTHONPATH
ENV PYTHONPATH=/workspaces/proj

# Set the working directory
WORKDIR /workspaces/proj

# Switch to the non-root user
USER vscode

# Latest version of pip tooling
RUN pip install --upgrade pip
