import os
import json
from superset.app import create_app
from superset import db

app = create_app()

with app.app_context():
    # Import sau khi app context đã sẵn sàng
    from superset.models.core import Database

    # Đọc file JSON
    with open("/app/docker-entrypoint-initdb.d/supabase.json") as f:
        data = json.load(f)

    for db_info in data:
        uri = db_info["sqlalchemy_uri"].replace("${SUPABASE_PASSWORD}", os.environ["SUPABASE_PASSWORD"])

        # Nếu database chưa tồn tại
        if not db.session.query(Database).filter_by(database_name=db_info["database_name"]).first():
            db_obj = Database(database_name=db_info["database_name"], sqlalchemy_uri=uri)
            db.session.add(db_obj)
            db.session.commit()
            print(f"Database {db_info['database_name']} imported!")
        else:
            print(f"Database {db_info['database_name']} already exists.")
