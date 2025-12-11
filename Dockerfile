# Use a pre-built image with ML packages already installed
FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-runtime

# Set working directory
WORKDIR /app

# Install additional packages
RUN pip install --no-cache-dir transformers psycopg2-binary

# Copy project files
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Default command
CMD ["python", "cli.py", "--help"]