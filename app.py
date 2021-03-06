from flask import Response, render_template, jsonify, request
from application import APP

@APP.route('/')
def index():
    return render_template(
        'index.html'
        )


if __name__ == '__main__':
    APP.debug = True
    APP.run()