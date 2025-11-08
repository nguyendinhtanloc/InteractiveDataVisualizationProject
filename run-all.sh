#!/bin/bash

echo "Setting up Python virtual environment"

if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "Virtual environment 'venv' created."
fi

source venv/bin/activate
pip install --upgrade pip

if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    echo "Python dependencies installed."
fi

echo "Starting Docker Compose"
docker-compose up -d

echo "Done! Superset should be running at http://localhost:8088"
echo "Default admin credentials: ${SUPERSET_USERNAME} / ${SUPERSET_PASSWORD}"
