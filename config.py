import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", f"sqlite:///{os.path.join(BASE_DIR, 'dental.db')}")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.0-flash"
DEVELOPER_INFO = {"name": "Dr. Hothaifa Al-Hamdani", "phone": "+967 770972786", "email": "hothaifaalhamdani123@gmail.com", "clinic": "Dental Hothaifa Clinic"}
