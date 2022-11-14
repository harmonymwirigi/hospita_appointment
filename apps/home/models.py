# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from datetime import datetime, time
from apps import db
class AppointMent(db.Model):
    __tablename__ = 'AppointMent'
    id = db.Column(db.Integer, primary_key=True)
    Date = db.Column(db.Date(), nullable = False)
    Time = db.Column(db.Time(), nullable = False)
    questions = db.relationship('Question', backref='appointment', lazy=True)
    weight = db.Column(db.Integer, nullable = False)
    height = db.Column(db.Integer, nullable = False)
    Age = db.Column(db.Integer, nullable = False)
    Name = db.Column(db.String(30), nullable = False)
    Phoneno = db.Column(db.String(15), nullable = False)
    status = db.Column(db.Boolean, default = False)
    made_by = db.Column(db.Integer, db.ForeignKey('Users.id'))
    made_to = db.Column(db.Integer, db.ForeignKey('Doctors.id'))


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    my_appointment = db.Column(db.Integer, db.ForeignKey('AppointMent.id'))
    question = db.Column(db.String(100))

    def __repr__(self):
        return f'{self.question}'