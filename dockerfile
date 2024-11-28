# Use Python 3.10 slim as base
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY pyproject.toml .
COPY setup.cfg .
COPY src/ src/
COPY tests/ tests/
COPY README.md .

# Install project dependencies
RUN pip install --no-cache-dir -e ".[test]"

# Set Python path for tests
ENV PYTHONPATH=/app/src

# Default command to run tests
CMD ["pytest", "tests/", "-v", "--cov=quantum_enhanced_lwe"]