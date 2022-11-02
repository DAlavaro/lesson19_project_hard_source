from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, id_):
        """
        Получение режиссера по ID
        """
        return self.session.query(Director).get(id_)

    def get_all(self):
        """
        Получение всех режиссеров
        """
        return self.session.query(Director).all()

    def create(self, director_d):
        """
        Создание режиссера
        """
        ent = Director(**director_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        """
        Удаление режиссера
        """
        director = self.get_one(rid)
        self.session.delete(director)
        self.session.commit()

    def update(self, director_d):
        """
        Обновление режиссера
        """
        director = self.get_one(director_d.get("id"))
        director.name = director_d.get("name")
        self.session.add(director)
        self.session.commit()
