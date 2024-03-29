from flask import Flask, request, jsonify
from dbconfig import db
from models import Welcoming

# Instanciate flask app
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fandango.db' # URI configuration (sqlite and fandango.db)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Associate db to flask app
db.init_app(app)

# Create all db tables under app context
with app.app_context():
    db.create_all()

@app.route('/welcoming', methods=['GET'])
def welcoming():
    name = request.args.get('name', 'World')
    message = f'Hello, {name}!'
    welcoming = Welcoming(name=name, message=message)
    db.session.add(welcoming)
    db.session.commit()
    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
