from flask import Flask, request, Response
from flask_cors import CORS
import json
from KSUser import KSUser
import requests

app = Flask(__name__)
CORS(app)

users= {}
key_servers=[]

@app.route("/login", methods=["POST"])
async def login():
    username = request.json['username']
    password = request.json['password']

    ks_user:KSUser = users.get(username)

    if(ks_user==None or ks_user.password!=password):
        return app.response_class(
        response=json.dumps({'response':'Wrong username or password!'}),
        status=403,
        mimetype='application/json')
    return app.response_class(
        response=json.dumps({'response':ks_user.get_private_key(password).save_pkcs1().decode('utf-8')}),
        status=200,
        mimetype='application/json')

@app.route("/create", methods=["POST"])
async def sign_up():
    username = request.json['username']
    password = request.json['password']
    if(users.get(username)==None):
        for server in key_servers:
            params={'username':username}
            response = await requests.post(server+"/get-public-key",params)
            if(response.status_code==200):
                return app.response_class(
                response=json.dumps({'response':'User with that username already exists!'}),
                status=409,
                mimetype='application/json')

        users[username] = KSUser(username,password)
        return app.response_class(
        response=json.dumps({'response':'User successfully created!'}),
        status=200,
        mimetype='application/json')
    else:
        return app.response_class(
        response=json.dumps({'response':'User with that username already exists!'}),
        status=409,
        mimetype='application/json')

@app.route("/get-public-key", methods=["POST"])
async def get_public_key():
    username = request.json['username']
    print(username)
    ks_user:KSUser = users.get(username)
    if(ks_user==None):
        for server in key_servers:
            params={'username':username}
            response = await requests.post(server+"/get-public-key",params)
            if(response.status_code==200):
                return app.response_class(
                response=json.dumps({'response':ks_user.get_public_key().save_pkcs1().decode('utf-8')}),
                status=200,
                mimetype='application/json')
        return app.response_class(
        response=json.dumps({'response':'Invalid username!'}),
        status=404,
        mimetype='application/json')
    return app.response_class(
        response=json.dumps({'response':ks_user.get_public_key().save_pkcs1().decode('utf-8')}),
        status=200,
        mimetype='application/json')


app.run(host="0.0.0.0", port=8000, threaded=True)