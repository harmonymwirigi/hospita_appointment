# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from apps import db
from apps.home.form import Appointment, CheckAppointment
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from jinja2 import TemplateNotFound
from apps.home.models import AppointMent, Question
from apps.authentication.models import Doctors


@blueprint.route('/index', methods = ['GET', 'POST'])
@login_required
def index():
    my_appointment = AppointMent.query.all()
    formm = Appointment(request.form)
    formm.Doctor.choices = [(hospital.Hospital) for hospital in Doctors.query.all()]
    if formm.validate_on_submit():
        doctor = Doctors.query.filter_by(Hospital = formm.Doctor.data).first()
        appointmentobj = AppointMent(made_by = current_user.id,made_to = doctor.id, Date= formm.Date.data,Time = formm.Time.data, weight = formm.weight.data,height = formm.height.data, Age = formm.Age.data, Name = formm.Name.data, Phoneno = formm.Phoneno.data)
        db.session.add(appointmentobj)
        db.session.commit()
        for i in formm.Question.data:
            print(i)
            question = Question(my_appointment = appointmentobj.id, question= i)
            db.session.add(question)
            db.session.commit()
        
        return redirect(url_for('home_blueprint.index'))
    return render_template('home/index.html', segment='index', form = formm, my_appointment = my_appointment)


@blueprint.route('/doctor')
@login_required
def doctor():
    appointments = AppointMent.query.filter_by(made_to = current_user.id).all()
    return render_template('home/doctor.html', segment='index', appointments = appointments)

@blueprint.route('/appointment/<id>', methods = ['POST', 'GET'])
@login_required
def appointment(id):
    appointment = AppointMent.query.filter_by(id = id).first()
    completeAppintment = CheckAppointment(request.form)
    if completeAppintment.validate_on_submit():
        appointment.status = True
        db.session.add(appointment)
        db.session.commit()
        return redirect(url_for('home_blueprint.doctor'))
    return render_template('home/appointment_profile.html', appointment = appointment, completeAppintment = completeAppintment)

@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
