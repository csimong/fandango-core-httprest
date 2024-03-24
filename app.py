from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///saludos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Saludo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    mensaje = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Saludo %r>' % self.nombre

# @app.before_first_request
def crear_tablas():
    db.create_all()
with app.app_context():
    db.create_all()

@app.route('/saludo', methods=['GET'])
def saludo():
    nombre = request.args.get('nombre', 'Mundo')
    mensaje = f'Hola, {nombre}!'
    saludo = Saludo(nombre=nombre, mensaje=mensaje)
    db.session.add(saludo)
    db.session.commit()
    return jsonify({'mensaje': mensaje})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
