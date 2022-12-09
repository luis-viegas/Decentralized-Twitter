import asyncio
import threading

from aioflask import Flask, request, Response
from flask_cors import CORS
from Node import Node

app = Flask(__name__)
CORS(app)

node = None

def set_node(node_received):
    global node
    node = node_received


@app.route("/login", methods=["POST"])
async def hello_world():
    user = request.json
    global node
    node.username = user["username"]
    print("you are now logged in as " + node.username)
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
