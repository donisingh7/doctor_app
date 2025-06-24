# backend/test_db.py
import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# 1. Load .env from current dir
load_dotenv()  

# 2. Read env vars
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASS}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# 3. Create engine & connect
engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    result = conn.execute(text("SELECT id, name FROM doctors;"))
    doctors = result.fetchall()
    print("Doctors table rows:")
    for doc in doctors:
        print(f"  id={doc.id}, name={doc.name}")
