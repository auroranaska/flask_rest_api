from app import db
from .experience_level.model import ExperienceLevel


class Person(db.Model):
    __tablename__ = 'person'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    size = db.Column(db.Float)
    weight = db.Column(db.Float)
    strong_hand = db.Column(db.Boolean) #left/right: false/true
    experience_id = db.Column(db.Integer, db.ForeignKey(ExperienceLevel.id), nullable=False)

    def __repr__(self):
        return 'Id: {}, name: {}, size:{}, weight: {}, strong_hand:{}, experience_id:{}'.format(self.id, self.name, self.size, self.weight, self.strong_hand, self.experience_id)
