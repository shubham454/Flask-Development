from flask import Flask,render_template,flash

app = Flask(__name__)
app.secret_key='shubham'
# @app.route('/')
# def m1():
#     flash('msg----1')
#     flash('msg----1')
#     flash('msg----1')
#     return render_template('index.html')
# if __name__=='__main__':
#     app.run(debug=True)

# @app.route('/')
# def m1():
#     flash('msg----1','success')
#     flash('msg----1','error')
#     flash('msg----1','warning')
#     return render_template('categorie.html')
# if __name__=='__main__':
#     app.run(debug=True)

@app.route('/')
def m1():
    flash('msg----1','success')
    flash('msg----1','error')
    flash('msg----1','warning')
    return render_template('success.html')
if __name__=='__main__':
    app.run(debug=True)
