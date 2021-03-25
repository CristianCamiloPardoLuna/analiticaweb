from flask import Response, render_template, jsonify, request
from application import APP

@APP.route('/')
def index():
    return render_template(
        'index.html'
        )

@APP.route('/pricing')
def pricing():
    return render_template(
        'pricing.html'
    )

@APP.route('/contact')
def contact():
    return render_template(
        'contactus.html'
    )


if __name__ == '__main__':
    APP.debug = True
    APP.run()