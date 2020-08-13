from flask import Flask,Blueprint
viewb = Blueprint('view',__name__)

@viewb.route('/')
def m1():
    return 'views from view'
