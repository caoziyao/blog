# coding: utf-8

from flask import  render_template
from flask.blueprints import Blueprint
from handlers.file_handler import listdir

app = Blueprint('edit', __name__, static_folder='static')


@app.route('/hello')
def edit():
    folder = 'wiki'
    dirs, files = listdir(folder)

    d = {
        'dirs': dirs,
        'files': files,
    }
    return render_template('edit_hello.html')