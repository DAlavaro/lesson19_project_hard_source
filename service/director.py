from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, id_):
        """
        Получение директора по ID
        """
        return self.dao.get_one(id_)

    def get_all(self):
        """
        Получение всех режиссеров
        """
        return self.dao.get_all()

    def create(self, director_d):
        """
        Создание режиссера
        """
        return self.dao.create(director_d)

    def update(self, director_d):
        """
        Обновление режиссера
        """
        self.dao.update(director_d)
        return self.dao

    def delete(self, id_):
        """
        Удаление режиссера
        """
        self.dao.delete(id_)