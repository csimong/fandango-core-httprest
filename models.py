from db import db

class Welcoming(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    message = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Welcoming %r>' % self.name