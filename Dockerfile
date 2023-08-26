# Use an official Python runtime as the base image
FROM python:3

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app/
COPY . /app/

# Expose port 8000 for the Django app
EXPOSE 8000

# Command to run your Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
