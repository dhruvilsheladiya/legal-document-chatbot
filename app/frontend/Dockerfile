# Use Python base image
FROM python:3.10

# Set working directory inside the container
WORKDIR /app/frontend

# Copy frontend application files
COPY . /app/frontend/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
