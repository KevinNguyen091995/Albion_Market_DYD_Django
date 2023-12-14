# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV DJANGO_SETTINGS_MODULE=albion_django.settings

# Run app.py when the container launches
CMD ["gunicorn", "albion_django.wsgi:application", "--bind", "0.0.0.0:8000"]
