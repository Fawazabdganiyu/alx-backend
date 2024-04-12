#!/usr/bin/env python3
"""
Flask application definition
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Optional, Dict


class Config:
    """ Configure available languages and default settings
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> Optional[str]:
    """ Get the best match supported language from user browser
    """
    requested_locale = request.args.get("locale")
    if requested_locale in app.config['LANGUAGES']:
        return requested_locale

    if g.user:
        user_setting_locale = g.user.get('locale')
        if user_setting_locale in app.config['LANGUAGES']:
            return user_setting_locale
    header_locale = request.accept_languages.best_match(
        app.config['LANGUAGES']
    )
    if header_locale:
        return header_locale
    return app.config['BABEL_DEFAULT_LOCALE']


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Optional[Dict]:
    """Get a user dictionary"""
    user_id = request.args.get('login_as')
    return users.get(int(user_id)) if user_id else None


@app.before_request
def before_request():
    """Set a logged-in user for the app"""
    g.user = get_user()


@app.route('/', strict_slashes=False)
def index() -> str:
    """ Welcome page
    """
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
