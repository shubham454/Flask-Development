from flask import Flask
from models.login import loginb,error404
from views.view import viewb

app = Flask(__name__)

app.register_blueprint(loginb)
app.register_blueprint(viewb)

# @app.errorhandler(404)
# def abc(error):
#     return 'dhajdafkafkafasf'

app.register_error_handler(404,error404)
if __name__ == '__main__':
    app.run(debug=True)
