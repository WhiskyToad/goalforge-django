# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /src

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /src/
COPY . /src/
COPY wait-for-postgres.sh /src/
RUN chmod +x /app/wait-for-postgres.sh


# Specify the command to run on container start
CMD ["gunicorn", "yourproject.wsgi:application", "--bind", "0.0.0.0:8000"]
