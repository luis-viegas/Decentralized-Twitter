import asyncio
import threading

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
async def hello_world():
    user = request.json
    global node
    node.username = user["username"]
    print("you are now logged in")
    return str(node.username)

@app.route("/tweet", methods=["POST"])
async def tweet():
    tweet = request.json
    global node
    await node.tweet(tweet["text"])
    print("you posted a tweet")
    return "Tweet posted successfully"