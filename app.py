from flask import Response, render_template, jsonify, request
from datetime import datetime
from application import APP
from application.backend.models import Contact, Stage1, db

@APP.route('/')
def index():
    return render_template(
        'index.html'
        )

@APP.route('/startnow', methods=['POST'])
def startnow():
    email = request.form.get('email')
    tellusmore = str('¡Quiero iniciar mi primer proyecto con Analítica!')
    newContact = Stage1(
        email = email,
        datetime = datetime.now()
    )
    db.session.add(newContact)
    db.session.commit()
    return render_template(
        'contactus.html',
        email = email,
        tellusmore = tellusmore
    )

@APP.route('/pricing')
def pricing():
    return render_template(
        'pricing.html'
    )

@APP.route('/get_your_plan/<_plan>')
def plans(_plan):
    _dict = {1:'Básico', 2:'Profesional', 3:'Empresarial'}
    tellusmore = str('Quiero adquirir el paquete {} y empezar la transformación digital de mi empresa.').format(_dict[int(_plan)])
    return render_template(
        'contactus.html',
        tellusmore = tellusmore
    )

@APP.route('/contact', methods=['GET','POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    company = request.form.get('company')
    service = request.form.get('service')
    tellusmore = request.form.get('tellusmore')

    newContact = Contact(
        name = name,
        email = email,
        company = company,
        service = service,
        tellusmore = tellusmore,
        datetime = datetime.now()
    )

    db.session.add(newContact)
    db.session.commit()

    return render_template(
        'contactus.html'
    )


if __name__ == '__main__':
    APP.debug = True
    APP.run()