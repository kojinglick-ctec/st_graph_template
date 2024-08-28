# Use an official Python 3.12 runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Define environment variable
# ENV NAME World

# Run app.py when the container launches
CMD ["streamlit", "run", "app.py"]
