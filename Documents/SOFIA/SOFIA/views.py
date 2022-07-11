"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask, render_template, jsonify, request, flash
from werkzeug.utils import secure_filename
from SOFIA import app
import os



# maximum filesize in megabytes
file_mb_max = 40

#app.config["UPLOAD_FOLDER"] = "uploads"
# full path destination for our upload files
rutadestino = os.path.join(os.getcwd(), 'uploads')
filename = None

app.config['MAX_CONTENT_LENGTH'] = file_mb_max * 1024 * 1024

ALLOWED_EXTENSIONS = set (['xml'])
def allowed_file(file):
    file = file.split('.')
    print(file)
    if file[1] in ALLOWED_EXTENSIONS:
        return True
    return False

@app.route('/upload', methods =['POST'])
def uploadfile():    
    file = request.files["uploadFile"]
    print(file, file.filename)
    filename = secure_filename(file.filename)
    print(file.filename)
    if file and allowed_file(filename):       
        file.save(os.path.join(rutadestino , filename))
        return render_template('index.html', message_text='Archivo cargado exitosamente')


       


@app.route('/')
#@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Sofia',
        #year=datetime.now().year,
    )

