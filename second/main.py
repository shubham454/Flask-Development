from flask import Flask,render_template,redirect,request

app = Flask(__name__)

# @app.route('/')
# def hello():
#     return render_template('home.html')

@app.route('/', methods=['GET','POST'])
def Show_view():
    if request.method=="POST":
        eno = request.form.get('eno')
        ename = request.form.get('ename')
        esalary = request.form.get('esalary')
        eaddrs = request.form.get('eaddrs')
        context = {'eno':eno,'ename':ename,'esalary':esalary,'eaddrs':eaddrs}
        return render_template('home.html',context = context)
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
