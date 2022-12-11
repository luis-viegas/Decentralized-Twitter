import asyncio
import threading
import rsa

from flask import Flask, request, Response
from flask_cors import CORS
from Node import Node

app = Flask(__name__)
CORS(app)

node = None

def set_node(node_received):
    global node
    node = node_received


@app.route("/login", methods=["POST"])
async def login():
    user = request.json
    global node
    await node.login(user["username"],rsa.PrivateKey.load_pkcs1(user["private_key"]),rsa.PublicKey.load_pkcs1(user['public_key']))
    return str(node.username)

@app.route("/tweet", methods=["POST"])
async def tweet():
    tweet = request.json
    global node
    await node.tweet(tweet["text"])
    print("you posted a tweet : " + node.username)
    return "Tweet posted successfully"

@app.route("/timeline", methods=["GET"])
async def timeline():
    global node
    result = await node.get_timeline()
    print(node.user.tweets)
    return result

@app.route("/follow", methods=["POST"])
async def follow():
    username = request.json
    global node
    if not (await node.follow(username["username"])):
        return "User not found"
    print("you followed someone")
    return "Successfully followed " + username["username"]

@app.route("/unfollow", methods=["POST"])
async def unfollow():
    username = request.json
    global node
    if not (await node.unfollow(username["username"])):
        return "User not found"
    print("you unfollowed someone")
    return "Successfully unfollowed " + username["username"]

@app.route("/logout", methods=["GET"])
async def logout():
    global node
    node.logout()
    return "Logged out successfully"

@app.route("/following", methods=["GET"])
async def following():
    global node
    result = await node.get_following()
    return result