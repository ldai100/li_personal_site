from flask import Flask, render_template, request, send_file
from wsgiref.simple_server import make_server

import logging
import logging.handlers
import resources
import resources_pm

application = Flask(__name__)


@application.route('/resume/')
def download_resume():
    return send_file('static/old/downloads/li_resume.pdf', as_attachment=True, attachment_filename='li_resume.pdf')


@application.route('/old', methods=['GET'])
def get_old():
    return render_template('index_old.html', text=resources.text)


@application.route('/', methods=['GET'])
def init():
    return render_template('index.html', text=resources_pm.text)


if __name__ == "__main__":
    application.add_url_rule('/static_pm/<path:filename>', endpoint='static_pm',
                             view_func=application.send_static_file)
    application.run()
