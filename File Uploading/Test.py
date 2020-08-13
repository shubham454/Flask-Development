import os
from flask import Flask, flash, request, redirect, render_template, url_for
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


UPLOAD_FOLDER = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), 'file')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'yogeshinde#12'


@app.route('/')
def upload_form():
    return render_template('file.html')


@app.route('/upload', methods=['GET', 'POST'])
def fileupload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No File Attached')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No Selected File')
            return redirect(request.url)
        if file:
            fname = secure_filename(file.filename)
            if allowed_file(file.filename):
                # print(fname,app.config['UPLOAD_FOLDER'])
                # print(os.path.join(app.config['UPLOAD_FOLDER'],fname))
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], fname))
                return 'File Uploaded Successfully'
            flash(
                f'File extention not matched. It should be {ALLOWED_EXTENSIONS}')
            return redirect(request.url)
    return render_template('file.html')


if __name__ == '__main__':
    app.run(debug=True)
