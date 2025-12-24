#!/bin/bash
set -e

# Upgrade DB
superset db upgrade

# Tạo admin user
superset fab create-admin \
    --username "${SUPERSET_USERNAME}" \
    --password "${SUPERSET_PASSWORD}" \
    --firstname Superset \
    --lastname Admin \
    --email admin@example.com

# Khởi tạo Superset
superset init

# Start Superset
exec gunicorn -w 10 -b 0.0.0.0:8088 "superset.app:create_app()"
