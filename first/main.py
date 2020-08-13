from flask import Flask, render_template,redirect
from flask import request
data = {}
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    print(data)
    if request.method == "POST":
        uname = request.form.get('uname')
        password = request.form.get('password')
        if data.get(uname) == password:
            return 'you are logged in '
        elif data.get(uname) != password:
            return 'not match'
    return render_template("login.html")

@app.route('/register/',methods=['GET','POST'])
def register():
    if request.method=='POST':
        uname = request.form.get('uname')
        name = request.form.get('name')
        password = request.form.get('password')
        if uname in data.keys():
            return 'username already exist'
        data[uname]=password
        return 'you added successfully'
    return render_template('register.html')
if __name__=='__main__':
    app.run(debug=True)
