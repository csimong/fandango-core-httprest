from flask import Flask, request, jsonify
from db import db
from views import register_views

# Instanciate flask app
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fandango-core.db' # URI configuration (sqlite and fandango.db)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Associate db to flask app
db.init_app(app)

# Create all db tables under app context
with app.app_context():
    db.create_all()

register_views(app)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
