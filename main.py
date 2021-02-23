import sys
import os
import pymongo
import cloudinary
from bson import ObjectId
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session
from datetime import datetime
from google.oauth2 import id_token
from google.auth.transport import requests
from werkzeug.utils import secure_filename 
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
from requests import Session

cloudinary.config(
  cloud_name = 'doh1zxka2',  
  api_key = '925166118213228',  
  api_secret = '7X20V3Zr2JtJMY753BkR1p1O8QQ'  
)

app = Flask(__name__)
uri = 'mongodb+srv://root:root@cluster0.b3ou3.mongodb.net/web?retryWrites=true&w=majority'
client = pymongo.MongoClient(uri)
db = client.get_default_database()
app.secret_key = 'very-secret-key'

@app.route('/', methods=['GET'])
def default():
    pr = db['pr']
    lista = pr.find()
    return render_template('listado.html', lista=lista)
 
@app.route('/nuevo', methods=['GET','POST'])
def nuevo():
    if request.method == 'GET':
        return render_template('nuevo.html')
    else:
        pr=db['pr']
        msg = {'empresa': request.form['empresa'],
            'cod': request.form['cod'],
            'plazas' : request.form['plazas'], 
            'meses': request.form['meses'],
            'sueldo': request.form['sueldo'],
            'mod' : request.form['mod'], 
            'dir': request.form['dir'],
            'detalle': request.form['detalle'],
            'req' : request.form['req']
        }
        pr.insert_one(msg)
        return redirect('/')
  

@app.route('/ver/<id>', methods=['GET'])
def ver(id):
    if request.method == 'GET':
        pr= db['pr']
        men=pr.find_one({'_id':ObjectId(id)})
        return render_template('ver.html',res=men)
  

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True) 