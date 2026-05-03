# Use the 'slim' version for a much smaller image size (faster deployments)
FROM python:3.10-slim

WORKDIR /app

# BEST PRACTICE: Copy ONLY requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies before copying the rest of the code
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of your application code
COPY . .

EXPOSE 10000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "10000"]