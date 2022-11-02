from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from implemented import user_service

user_ns = Namespace('user')


@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        """
        Формирование представления для получения всех пользователей
        """
        users = user_service.get_all()
        result = UserSchema(many=True).dump(users)
        return result, 200

    def post(self):
        """
        Формирование представления для добавления новых пользователей
        """
        req_json = request.json
        user_service.create(req_json)
        return "", 201


@user_ns.route('/<int:id_>')
class UserView(Resource):
    def get(self, id_):
        """
        Формирование представления для получения пользователя по ID
        """
        user = user_service.get_one(id_)
        result = UserSchema().dump(user)
        return result, 200

    def put(self, id_):
        """
        Формирование представления для изменения данных пользователя
        """

        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = id_
        user_service.update(req_json)
        return "", 204

    def delete(self, id_):
        """
        Формирование представления для удаления пользователя по ID
        """
        user_service.delete(id_)
        return "", 204
