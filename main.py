from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from werkzeug.utils import secure_filename
from flask import jsonify
from script_generar_reporte.create_html_report import generate_report
from flask import flash
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'script_generar_reporte')
app.config['UPLOAD_EXTENSIONS'] = ['.xml']


def file_validation(file_name):
    path_file, file_extension = os.path.splitext(file_name)
    if file_extension in app.config['UPLOAD_EXTENSIONS']:
        return True
    return False


@app.route('/')
def index_html():
    return render_template('index.html')


@app.route('/upload_file', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and file_validation(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
            return render_template('progress_report.html', file_name = file.filename)
        return '<h1 style="text-align:center; color: #EB1D36; margin-top:80px; font-size:40px">Not file selected or file extesnsion is incorrect</h1>'


@app.route('/generate_html_report', methods=['POST'])
def generate_html_report():
    if request.method == 'POST':
        data_recvd = request.json
        xml_file_name = data_recvd['fileName']
        xml_path = os.path.join(os.getcwd(), 'script_generar_reporte\{}'.format(xml_file_name))
        generate_report(xml_path)
    return jsonify(code_response = 400)
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8082)
