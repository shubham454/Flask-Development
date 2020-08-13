from flask import Flask,render_template,abort
app = Flask(__name__)

@app.route('/')
def m1():
    return render_template('index.html')

@app.route('/<name>')
def m2(name):
    if name[0].isdigit():
        abort(404)
    return render_template('index.html')

@app.errorhandler(404)
def error_404(error):
    return render_template('error404.html')

@app.errorhandler(500)
def error_500(error):
    return render_template('error500.html')

if __name__ == '__main__':
    app.run(debug=True)
