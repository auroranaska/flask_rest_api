from app import db


class ExperienceLevel(db.Model):
    __tablename__ = 'experience_level'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return 'Id: {}, name: {}'.format(self.id, self.name)
