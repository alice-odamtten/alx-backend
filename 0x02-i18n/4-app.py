#!/usr/bin/env python3
'''setup a basic Flask app'''
from flask import Flask, render_template
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)


class Config:
    '''a class config'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    '''determine the best match with our supported languages'''
    if 'locale' in request.args and request.args['locale'] in app.config['LANGUAGES']:
        return request.args['locale']

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    '''returns hello world'''
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
