import asyncio
import sys
import threading

from Node import Node
from backend import set_node, app
from config import FLASK_PORT


def run_node(node):
    asyncio.run(node.run())

def run_backend(node):
    set_node(node)

    app.run(host=node.node_ip, port=FLASK_PORT + node.node_id, threaded=True)


def run_proccess(id):
    node = Node(int(id))

    node_thread = threading.Thread(target=run_node, args=(node,))
    backend_thread = threading.Thread(target=run_backend, args=(node,))
    node_thread.start()
    backend_thread.start()

    print("Node " + str(id) + " started")

    node_thread.join()
    backend_thread.join()




if (sys.argv[1] == "node"):
    id = sys.argv[2]
    run_proccess(id)



