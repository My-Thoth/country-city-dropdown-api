# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Initialize the db object
db = SQLAlchemy()

def create_app():
    # Load environment variables
    load_dotenv()

    # Get database connection details from .env
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_NAME = os.getenv('DB_NAME')
    DB_USER = os.getenv('DB_USER')
    DB_PASS = os.getenv('DB_PASS')

    # Create the PostgreSQL connection string
    DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    # Initialize the Flask app
    app = Flask(__name__)

    # Configure the SQLAlchemy part of the app
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize SQLAlchemy and connect to the app
    db.init_app(app)

    # Pass both app and db to initialize routes
    from app.routes import initialize_routes
    initialize_routes(app, db)

    return app # Return both app and db