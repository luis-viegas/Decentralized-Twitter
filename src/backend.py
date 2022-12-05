from flask import Flask, request, Response
from flask_cors import CORS
from Node import Node

app = Flask(__name__)
CORS(app)

node = None

def set_node(node_received):
    global node
    node = node

@app.route("/login", methods=["POST"])
async def hello_world():
    user = request.json
    global node
    node = Node(1, user["username"])
    await node.run()
    print("you are now logged in")
    return "Hello, World!"

@app.route("/tweet", methods=["POST"])
async def tweet():
    global node
    await node.tweet("hello from frontend")
    print("you posted a tweet")
    return "Tweet posted"