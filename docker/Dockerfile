FROM python:3.10-slim

# -------------------------
# SYSTEM DEPENDENCIES
# -------------------------

RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    ffmpeg \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# -------------------------
# WORK DIRECTORY
# -------------------------

WORKDIR /app

# -------------------------
# COPY FILES
# -------------------------

COPY requirements.txt .

# -------------------------
# INSTALL PYTHON PACKAGES
# -------------------------

RUN pip install --no-cache-dir -r requirements.txt

# -------------------------
# COPY PROJECT
# -------------------------

COPY . .

# -------------------------
# EXPOSE PORT
# -------------------------

EXPOSE 8000

# -------------------------
# RUN APPLICATION
# -------------------------

CMD ["python", "run.py"]