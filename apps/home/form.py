# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField,validators, TimeField, IntegerField, SubmitField, SelectMultipleField, widgets
from wtforms.validators import DataRequired

class Questions(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget =widgets.CheckboxInput() 

class Appointment(FlaskForm):
    Doctor = SelectField('Hospital', validators=[DataRequired()])
    Phoneno = StringField('Phone Number', validators=[DataRequired()])
    Name = StringField('FULL NAME', validators=[DataRequired()])
    Date = DateField('Date', format='%Y-%m-%d', validators = [validators.DataRequired()])
    Time = TimeField('TIME', validators=[DataRequired()])
    weight = IntegerField('WEIGHT IN KG', validators = [DataRequired()])
    height = IntegerField("HEIGHT IN METERS", validators=[DataRequired()])
    Age = IntegerField('AGE', validators=[DataRequired()])
    Question = Questions('Questions', choices=[("Question1?"),("question2?"),("question3?")])
    Submit = SubmitField('BOOK')

class CheckAppointment(FlaskForm):
    Check = SubmitField('Done')