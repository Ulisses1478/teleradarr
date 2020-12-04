# Use the official Python image from the Docker Hub
FROM python:3.8.5

# These two environment variables prevent __pycache__/ files.
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Make a new directory to put our code in.
RUN mkdir /teleradarr

COPY app /teleradarr/app

COPY requirements.txt __init__.py startBot.py /teleradarr/


# Change the working directory.
# Every command after this will be run from the /hevex directory.
WORKDIR /teleradarr

# Upgrade pip
RUN pip install --upgrade pip

# Install the requirements.
RUN pip install -r requirements.txt


# Start server
CMD ["python", "startBot.py"]
