# Use the official Python 3.11 image from the Docker Hub
FROM python:3.11-alpine

# Create app directory (with user)
RUN addgroup -S app && adduser -S app -G app
WORKDIR /home/app

# Install dependencies
# First copy requirements.txt and install 
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy app
COPY . .

# Use an unprivileged user.
RUN mkdir -p /home/app/uploads && chown app:app /home/app/uploads
USER app

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
