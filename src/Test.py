import Node
import Origin
import asyncio
import threading
from multiprocessing import Process
from time import sleep
from backend import app
from backend import set_node
from config import FLASK_PORT

def run_node(node):
    asyncio.run(node.run())

def run_backend(node):
    set_node(node)

    app.run(host=node.node_ip, port=FLASK_PORT + node.node_id, threaded=True)

def run_proccess(index):
    node = Node.Node(index)

    node_thread = threading.Thread(target=run_node, args=(node,))
    backend_thread = threading.Thread(target=run_backend, args=(node,))
    node_thread.start()
    backend_thread.start()

    node_thread.join()
    backend_thread.join()

if __name__ == '__main__':

    #multiprocessing.Process(target=Origin.start).start()
    threading.Thread(target=Origin.run).start()

    sleep(1)


    p1 = Process(target=run_proccess, args=(1,))
    p2 = Process(target=run_proccess, args=(2,))
    p3 = Process(target=run_proccess, args=(3,))
    p1.start()
    p2.start()
    p3.start()

