from flask import request, jsonify
from dbconfig import db
from models import Welcoming

def register_views(app):
    @app.route('/welcoming', methods=['GET'])
    def welcoming():
        name = request.args.get('name', 'World')
        message = f'Hello, {name}!'
        welcoming = Welcoming(name=name, message=message)
        db.session.add(welcoming)
        db.session.commit()
        return jsonify({'message': message})
