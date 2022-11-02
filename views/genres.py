from flask import request
from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service
from utils import admin_required, auth_required

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        """
        Формирование представления для получения жанров
        """
        rs = genre_service.get_all()
        res = GenreSchema(many=True).dump(rs)
        return res, 200

    @admin_required
    def post(self):
        """
        Формирование представления для добавления новых пользователей
        """
        req_json = request.json
        genre_service.create(req_json)
        return "", 201


@genre_ns.route('/<int:rid>')
class GenreView(Resource):
    @auth_required
    def get(self, rid):
        """
        Формирование представления для получения жанра по ID
        """
        r = genre_service.get_one(rid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200

    @admin_required
    def put(self, id_):
        """
        Формирование представления для изменения жанра
        """

        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = id_
        genre_service.update(req_json)
        return "", 204

    @admin_required
    def delete(self, id_):
        """
        Формирование представления для удаления жанра по ID
        """
        genre_service.delete(id_)
        return "", 204
