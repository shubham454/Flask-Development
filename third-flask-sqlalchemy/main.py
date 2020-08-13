from flask import Flask,request,render_template,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@localhost:3306/shubham'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
db = SQLAlchemy(app)

class User(db.Model):
    uid = db.Column(db.Integer,primary_key=True,unique=True)
    uname = db.Column(db.String(20))
    uaddr = db.Column(db.String(40))
    def __init__(self,uname,uaddr,uid):
        self.uname = uname
        self.uaddr = uaddr
        self.uid = uid
@app.route('/',methods=['GET','POST'])
def home_view():
    if request.method=='POST':
        uid = request.form.get('uid')
        uname = request.form.get('uname')
        uaddr = request.form.get('uaddr')
        user = User(uid=uid,uname=uname,uaddr=uaddr)
        db.session.add(user)
        db.session.commit()
        return render_template('userlist.html')
    return render_template('userlist.html')

@app.route('/fetchdata',methods=['GET','POST'])
def fetchdata():
    userlist = User.query.all()
    # userlist = db.session.query(User).all()
    return render_template('userlist.html',user = userlist)

@app.route('/update/<int:uid>/',methods=['GET','POST'])
def update(uid):
    user = User.query.get(uid)
    if request.method == "POST":
        print(user.uid,user.uname,user.uaddr)
        user.uname=request.form.get('uname')
        user.uaddr=request.form.get('uaddr')
        print(user.uname,user.uaddr)
        db.session.commit()
        return redirect('/fetchdata')
    return render_template('update.html',user=user)

@app.route('/delete/<int:uid>/',methods=['GET','POST'])
def delete(uid):
    user=User.query.get(uid)
    db.session.delete(user)
    db.session.commit()
    return redirect('/fetchdata')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
