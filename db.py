from flask_sqlalchemy import SQLAlchemy

# Instanciate SQLAlchemy
db = SQLAlchemy() 

# DB Models
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    details = db.Column(db.String(1200), nullable=False)

    def __repr__(self):
        return '<Project %r>' % self.id

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'details': self.details,
        }

# DB Functions
def createproject(project_id):
    print(f'Creating project with ID {project_id}')

    # Create new Project instance
    new_project = Project(id=project_id, name='prueba', details='prueba')

    # Add Project instance to db session and commit
    db.session.add(new_project)
    db.session.commit()
    print('Created successfully.')

def deleteproject(project_id):
    print(f'Deleting project with ID {project_id}')

    # Get Project instance by id
    project = Project.query.get(project_id)

    # Delete Project from db session and commit
    db.session.delete(project)
    db.session.commit()
    print('Deleted successfully.')
