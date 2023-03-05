import flask
import os
import json
import logParser
from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config["DEBUG"] = False
app.config["JSON_SORT_KEYS"] = False
app.config['UPLOAD_FOLDER'] = "/tmp"

@app.route('/api/v1/log-parser/', methods=['GET'])
def home():
    return "<h1>Log Parser API</h1> Options:<br>View Sample Result: /api/v1/log-parser/sample/ <br><br>Upload File: /api/v1/log-parser/file-upload"

@app.route('/api/v1/log-parser/sample/', methods=['GET'])
def sample_parser():
    file_path = "/tmp/sample.txt"
    a = logParser.main(file_path)
    return a

@app.route('/api/v1/log-parser/file-upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        a = jsonify({'message' : 'No file is attached'})
        return a
    f = request.files['file']
    f_name = secure_filename(f.filename)
    f_path = os.path.join(app.config['UPLOAD_FOLDER'], f_name)
    f.save(f_path)
    a = logParser.main(f_path)
    return a

                                                      

@app.route('/api/v1/log-parser/healthz')
def healthz():
    return "OK"
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
