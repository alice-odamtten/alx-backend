#!/usr/bin/env python3
'''setup a basic Flask app'''
from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)


class Config:
    '''a class config'''

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


users = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
        4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
        }


def get_user():
    '''get user'''
    user = request.args.get("login_as")
    if not user:
        return None
    for id, name in users.item():
        if id == int(user):
            return name
    return None


@app.before_request
def before_request():
    '''get user'''
    g.user = get_user()


@babel.localeselector
def get_locale():
    '''determine the best match with our supported languages'''
    locale = request.args.get("locale")
    if locale in Config.LANGUAGES:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    '''returns hello world'''
    return render_template('5-index.html', user=g.user)


if __name__ == '__main__':
    app.run(debug=True)
