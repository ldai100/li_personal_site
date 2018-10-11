from flask import Flask, render_template, request, send_file
from wsgiref.simple_server import make_server

import logging
import logging.handlers
import resources


application = Flask(__name__)

@application.route('/resume/')
def download_resume():
	return send_file('./static/downloads/li_resume_10_08.pdf', as_attachment=True, attachment_filename='li_resume')

@application.route('/', methods=['GET', 'POST'])
def init():
    return render_template('index.html', text=resources.text)

if __name__ == "__main__":
    application.run()