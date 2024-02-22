from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

dev_team_users = {
    "data_scientist": {
        "name": "Katja"
    },
    "product_owner": {
        "name": "Felix"
    }
}

management_team_users = {
    "project_lead": {
        "name": "Lena Mustermann"
    },
    "team_lead": {
        "name": "Max Mustermann"
    }
}


class AllUsers(Resource):
    def get(self):
        merged_object = dict()
        merged_object.update(dev_team_users)
        merged_object.update(management_team_users)
        return {'data': merged_object}, 200


class DevUsers(Resource):
    def get(self):
        return {'data': dev_team_users}, 200

    def post(self):
        # Hier Logik um einen neuen Nutzer anzulegen. Daraufhin schicken wir dann die Bestätigung, dass der
        # Nutzer angelegt wurde. Dafür nutzen wir auch den Code 201 (201 Created)
        return {'data': "New User created"}, 201

    def delete(self):
        # Hier Logik um einen Nutzer zu löschen
        return {'data': "User deleted"}, 200


class ManagementUsers(Resource):
    def get(self):
        return {'data': management_team_users}, 200


api.add_resource(AllUsers, '/allusers')
api.add_resource(DevUsers, '/devusers')
api.add_resource(ManagementUsers, '/managementusers')

if __name__ == '__main__':
    app.run()
