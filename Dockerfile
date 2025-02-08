FROM python:3.9-slim

# Installer les dépendances système nécessaires à Pygame
RUN apt-get update && apt-get install -y \
    python3-dev \
    libfreetype6-dev \
    libSDL1.2-dev \
    libsdl-mixer1.2 \
    libsdl-ttf2.0-0 \
    libportmidi0 \
    && rm -rf /var/lib/apt/lists/*

# Copier les fichiers nécessaires dans l'image Docker
COPY requirements.txt .
COPY . .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Définir la commande de démarrage
CMD ["python", "main.py"]
