# coding: utf-8

from flask import  render_template
from flask.blueprints import Blueprint
from handlers.file_handler import FileHandler

app = Blueprint('edit', __name__, static_folder='static')


@app.route('/hello')
def edit():
    folder = 'wiki'
    f = FileHandler(folder)
    dirs, files = f.all_files()

    d = {
        'dirs': dirs,
        'files': files,
    }
    return render_template('edit_hello.html')