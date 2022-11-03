from flask import Flask,request,render_template,redirect,jsonify,session
import pymongo
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import requests
import psycopg2
import parsel
import json
import re


app  = Flask(__name__)
@app.route("/dataFromAjax",methods=['GET'])
def recv():
    data = request.args.get("head")
    if(data==""):
        return "0"

    else:
        print("收到客户{} ".format(data))
        return "1"


@app.route("/test",methods=['GET'])
def dasd():
    return render_template('test.html')

if __name__ == '__main__':
    app.run()