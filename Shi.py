#-*- coding: utf-8 -*-
import flask
from flask import Flask, render_template, request, redirect, url_for
#from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
@app.route("/")

def getPage():
    return render_template('Shi_flask.htm', **locals())

if __name__ == '__main__':
    app.run(debug=True).getPage()
    print("finished")    
