from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('first.html')
@app.route('/first')
def m1():
    return render_template('second.html')
@app.route('/second')
def m2():
    return render_template('third.html')
@app.route('/third')
def m3():
    return render_template('display.html')

if __name__=='__main__':
    app.run(debug=True)
