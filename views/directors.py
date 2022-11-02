from flask import request
from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from implemented import director_service
from utils import auth_required, admin_required

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        """
        Формирование представления для получения всех режиссеров
        """
        rs = director_service.get_all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200

    @admin_required
    def post(self):
        """
        Формирование представления для добавления новых пользователей
        """
        req_json = request.json
        director_service.create(req_json)
        return "", 201


@director_ns.route('/<int:ID>')
class DirectorView(Resource):
    @auth_required
    def get(self, id_):
        """
        Формирование представления для получения режиссера по ID
        """
        r = director_service.get_one(id_)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200

    @admin_required
    def put(self, id_):
        """
        Формирование представления для изменения данных режиссера
        """

        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = id_
        director_service.update(req_json)
        return "", 204

    @admin_required
    def delete(self, id_):
        """
        Формирование представления для удаления режиссера по ID
        """
        director_service.delete(id_)
        return "", 204
