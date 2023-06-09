import os

from flask import Flask, render_template, request

# pylint: disable=C0103
app = Flask(__name__)


@app.route('/')
def hello():
    if request.method == "POST":
        text = request.form["heart"]

    """Return a friendly HTTP greeting."""
    message = 'Welcome! Resumate!!'

    return render_template('index.html',

                           message=message)


if __name__ == '__main__':
    app.run(debug=True)
