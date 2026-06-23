import os, json
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
DATABASE_PATH = os.path.join(BASE_DIR, "dental.db")
SQLALCHEMY_DATABASE_URI = f"sqlite:///{DATABASE_PATH}"
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.0-flash"
DEVELOPER_INFO = {"name": "Dr. Hothaifa Al-Hamdani", "phone": "+967 770972786", "clinic": "Dental Hothaifa Clinic"}
