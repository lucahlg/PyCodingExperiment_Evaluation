from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from dotenv import load_dotenv
import os
import mysql.connector

def create_app():
    # Load environment variables from .env file
    load_dotenv()

    app = Flask(__name__)
    CORS(app)
    api = Api(app, version='1.0', title='Smart Fridge API', description='API for Smart Fridge Application')

    # Database configuration
    app.config['DB_HOST'] = os.getenv('DB_HOST')
    app.config['DB_USER'] = os.getenv('DB_USER')
    app.config['DB_PASSWORD'] = os.getenv('DB_PASSWORD')
    app.config['DB_NAME'] = os.getenv('DB_NAME')

    # Register blueprints
    from .routes.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

def get_db_connection():
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    return connection

