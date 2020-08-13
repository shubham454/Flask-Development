from flask import Flask,render_template,request,session

app = Flask(__name__)
app.secret_key = 'shubham203'
@app.route('/')
def m1():
    return render_template('first.html')

@app.route('/first')
def m2():
    session['fd']=request.args.get('t1')
    return render_template('second.html')

@app.route('/second')
def m3():
    session['sd']=request.args.get('t2')
    return render_template('third.html')

@app.route('/third')
def fourth():
    return render_template('display.html')

if __name__ == '__main__':
    app.run(debug=True)
