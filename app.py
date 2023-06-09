import os

from flask import Flask, render_template, request
from executive_model import resumate_model as remo

# pylint: disable=C0103
app = Flask(__name__)
a = []


@app.route('/', methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        text = request.form["heart"]
        a, b, c = remo(text)
        return render_template('index.html', me=text, key=a, name=b, vision=c)
    else:
        message = 'Welcome! Resumate!!'
        return render_template('index.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)
