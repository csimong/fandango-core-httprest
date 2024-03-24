from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///welcomings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Welcoming(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    message = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Welcoming %r>' % self.name

# @app.before_first_request
def create_tables():
    db.create_all()
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
