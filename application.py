from flask import Flask
from flask import render_template
from wsgiref.simple_server import make_server

import logging
import logging.handlers
import resources


app = Flask(__name__)

@app.route('/')
def init():
    return render_template('index.html', text=resources.text)

if __name__ == "__main__":
    app.run()