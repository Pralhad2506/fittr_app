from sqlmodel import create_engine, Session
import os
from dotenv import load_dotenv
from sqlalchemy.exc import SQLAlchemyError

# Load environment variables from .env file
load_dotenv()

# Database variables from .env file, with fallback for missing values
DB_USER = os.getenv('DB_USER', 'default_user')
DB_PASS = os.getenv('DB_PASS', 'default_password')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '3306')  # Default MySQL port
DB_NAME = os.getenv('DB_NAME', 'default_db')

# Check if all necessary environment variables are provided
if not all([DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME]):
    raise ValueError("One or more environment variables for the database are missing!")

# Create MySQL URL using pymysql driver
mysql_url = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create engine with echo=True for debugging, set echo=False in production
try:
    engine = create_engine(mysql_url, echo=True)  # Set echo=False in production
except SQLAlchemyError as e:
    print(f"Error creating engine: {e}")

# Function to create a new session
def get_session():
    """Generate a new database session."""
    with Session(engine) as session:
        yield session