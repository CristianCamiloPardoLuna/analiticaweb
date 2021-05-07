from flask import Response, render_template, jsonify, request, flash
from flask_login import current_user
from datetime import datetime
from application import APP
from application.backend.models import Contact, Stage1, db

@APP.route('/')
def index():
    return render_template(
        'index.html'
        )

@APP.route('/returnContacts/<_id>/')
def returnContacts(_id):
    if str(_id) == '1020813231':
        return jsonify([[i.name, i.email, i.company, i.service, i.tellusmore, i.datetime] for i in Contact.query.all()])
    else:
        return Response('Invalid request', status=404) 
"""Returns contact in model
"""

@APP.route('/startnow', methods=['POST'])
def startnow():
    email = request.form.get('email')
    tellusmore = str('¡Quiero iniciar mi primer proyecto con Analítica por $40.000 COP la hora!')
    if len(email)>0:        
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


@APP.route('/contact')
def contact():
    return render_template(
        'contactus.html',
    )

@APP.route('/contact/<tellusmore>')
def contactInfo(tellusmore):
    print(tellusmore)
    return render_template(
        'contactus.html',
        tellusmore = tellusmore
    )

@APP.route('/contact/contactme', methods=['POST'])
def contactme():
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
        'thanks.html'
    )

@APP.route('/thanks')
def thanks():
    return render_template(
        'thanks.html'
    )

@APP.route('/underconstruction')
def uc():
    return render_template(
        'underconstruction.html'
    )

@APP.route('/packageinfo')
def packageinfo():
    return render_template(
        'packageinfo.html'
    )

@APP.route('/privacypolicy')
def privacypolicy():
    return render_template(
        'privacy.html'
    )

@APP.route('/terms')
def terms():
    return render_template(
        'termsconditions.html'
    )

if __name__ == '__main__':
    APP.debug = True
    APP.run()