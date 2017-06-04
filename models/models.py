from database import db

from .base import Base

class Victim(Base):
    nick_name = db.Column(db.String(100))
    phone_number = db.Column(db.String(100))


class Listener(Base):
    nick_name = db.Column(db.String(100))
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    skills = db.Column(db.relationship('ListenerSkill'))
    score = db.Column(db.Integer)

    def add_skills(self, skill):
        self.skills.append(skill)


class ListenerSkill(Base):
    listener_id = db.Column(db.Integer, db.ForeignKey('listener.id'))
    text = db.Column(db.String(100))


class VictimListener(Base):
    listener_id = db.Column(db.Integer, db.ForeignKey('listener.id'))
    victim_id = db.Column(db.Integer, db.ForeignKey('victim.id'))
    intensity = db.Column(db.Integer)
