import os, daemon
from flask import Flask, render_template, request, \
                  redirect, send_from_directory 
from werkzeug.utils import secure_filename
from func import root, get_hash, get_new_dir, find_path

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('main.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    file = request.files['upload']
    filename = secure_filename(file.filename)
    path = root + '/files/temps'
    file.save(os.path.join(path, filename))
    response = get_new_dir(filename)
    return render_template('main.html', response=response)

@app.route('/download', methods=['GET', 'POST'])
def download_file():
    file_hash = request.form.get('download')
    path, filename = find_path(file_hash)
    return send_from_directory(path, filename)

@app.route('/delete', methods=['GET', 'POST'])
def delete_file():
    file_hash = request.form.get('delete')
    path, filename = find_path(file_hash)
    os.remove(path+filename)
    os.rmdir(path)
    return main()
 
if __name__ == '__main__':
    with daemon.DaemonContext():
        app.run()
