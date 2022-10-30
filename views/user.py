from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from implemented import user_service

user_ns = Namespace('user')


@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        users = user_service.get_all()
        res = UserSchema(many=True).dump(users)
        return res, 200


    def post(self):
        req_json = request.json
        user = user_service.create(req_json)
        return "", 201, {"location": f"/users/{user.id}"}


@user_ns.route('/<int:id_>')
class UserView(Resource):
    def get(self, id_):
        user = user_service.get_one(id_)
        result = UserSchema().dump(user)
        return result, 200

    def put(self, id_):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = id_
        user_service.update(req_json)
        return "", 204

    def delete(self, id_):
        user_service.delete(id_)
        return "", 204
