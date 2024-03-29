from flask import request, jsonify
from db import db
from db import Project

def register_views(app):
    @app.route('/projects/', methods=['GET'])
    def get_projects():
            projects = Project.query.all()
            projects_list = [project.to_dict() for project in projects]
            return jsonify(projects_list)
