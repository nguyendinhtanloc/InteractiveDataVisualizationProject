import os

# Load secret key từ env
SECRET_KEY = os.environ.get("SUPERSET_SECRET_KEY", "temporary_secret_key")

# Các config khác có thể thêm sau
