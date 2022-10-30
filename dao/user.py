from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, id_):
        return self.session.query(User).get(id_)

    def get_all(self):
        return self.session.query(User).all()

    def create(self, user_d):
        ent = User(**user_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, id_):
        genre = self.get_one(id_)
        self.session.delete(genre)
        self.session.commit()

    def update(self, user_d):
        genre = self.get_one(user_d.get("id"))
        genre.name = user_d.get("name")

        self.session.add(genre)
        self.session.commit()

    def get_user_by_username(self, username):
        user = self.session.query(User).filter(User.username == username).one_or_none()
        return user
