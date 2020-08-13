from flask import Flask,Blueprint,abort

loginb = Blueprint('login',__name__)

@loginb.route('/log')
def m1():
    abort(500,description = "Internal Server")
    return 'Login from models'

@loginb.errorhandler(404)
def error404(error):
    return 'please '
