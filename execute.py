import argparse
from db import createproject, deleteproject
from app import app

def main():

    # Create parser
    parser = argparse.ArgumentParser(description='FandanGO Core application')

    # Create subparser for different actions
    subparsers = parser.add_subparsers(dest='action', help='Subactions available')

    # Subaction 'createproject'
    parser_create = subparsers.add_parser('createproject', help='Create a new project')
    parser_create.add_argument('--id', type=int, required=True, help='Project ID')

    # Subaction 'deleteproject'
    parser_delete = subparsers.add_parser('deleteproject', help='Delete an existing project')
    parser_delete.add_argument('--id', type=int, required=True, help='Project ID')

    # Save kown and unkown arguments
    fixed_args, additional_args = parser.parse_known_args()

    # Manage subactions
    with app.app_context():
        if fixed_args.action == 'createproject':
            createproject(fixed_args.id)
        if fixed_args.action == 'deleteproject':
            deleteproject(fixed_args.id)



if __name__ == "__main__":
    main()