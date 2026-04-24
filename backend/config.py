import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Cohere API Configuration
    COHERE_API_KEY = os.getenv('COHERE_API_KEY')
    COHERE_MODEL = os.getenv('COHERE_MODEL', 'command-r-plus-08-2024')
    COHERE_MAX_TOKENS = int(os.getenv('COHERE_MAX_TOKENS', 1000))
    COHERE_TEMPERATURE = float(os.getenv('COHERE_TEMPERATURE', 0.6))

    # Flask Configuration
    SECRET_KEY = os.getenv('SECRET_KEY', 'change-this-secret')
    DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 't')

    # File Upload Configuration
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5MB limit
    ALLOWED_EXTENSIONS = {'pdf', 'docx', 'doc', 'txt'}

    # MongoDB
    MONGO_URI = os.getenv('MONGO_URI')

# Make config object
config = Config()
