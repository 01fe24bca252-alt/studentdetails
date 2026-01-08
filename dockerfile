# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all project files
COPY . /app

# Install pytest
RUN pip install pytest

# Run tests first (CI step)
RUN pytest

# Run the student application
CMD ["python", "student.py"]
