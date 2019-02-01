from flask import Flask

app = Flask(__name__)

# To avoid circular imports
from app import routes
