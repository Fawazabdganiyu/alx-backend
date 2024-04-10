#!/usr/bin/env python3
"""
Flask application definition
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """ Configure available languages and default settings
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


def get_locale() -> str:
    """ Get the best match supported language from user browser
    """
    requested_locale = request.args.get("locale")
    if requested_locale in app.config['LANGUAGES']:
        return requested_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app, locale_selector=get_locale)


@app.route('/', strict_slashes=False)
def index() -> str:
    """ Welcome page
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
