from flask import Flask, render_template, make_response, request

app = Flask(__name__)


@app.route('/')
def m1():
    return render_template('first.html')


@app.route('/first')
def m2():
    fdata = request.args.get('t1')
    resp = make_response(render_template('second.html'))
    resp.set_cookie('fd', fdata)
    return resp


@app.route('/second')
def m3():
    sdata = request.args.get('t2')
    resp = make_response(render_template('third.html'))
    resp.set_cookie('sd', sdata)
    return resp


@app.route('/third')
def fourth():
    return render_template('display.html')


if __name__ == '__main__':
    app.run(debug=True)
