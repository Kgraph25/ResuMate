import os

import requests
from flask import Flask, render_template


# pylint: disable=C0103
app = Flask(__name__)


@app.route('/')
def hello():
    if requests.method == "POST":
        text = requests.form("heart")

    """Return a friendly HTTP greeting."""
    message = 'Welcome! Resumate!!'

    re
    return render_template('index.html',

                           message=message)


if __name__ == '__main__':
    app.run(debug=True)