#!/usr/bin/env python3
"""
Flask application definition
"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """ Configure available languages and default settings
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index():
    """ Welcome page
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
