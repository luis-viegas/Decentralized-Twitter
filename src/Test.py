import Node
import Origin
import asyncio
import threading
from multiprocessing import Process
from time import sleep
from backend import app

def run_node(node):
    asyncio.run(node.run())

def run_backend():
    app.run(host="127.0.0.1", port=5001, threaded=True)

if __name__ == '__main__':

    #multiprocessing.Process(target=Origin.start).start()
    threading.Thread(target=Origin.run).start()

    sleep(1)

    node1 = Node.Node(1, "node1")
    node2 = Node.Node(2, "node2")

    p1 = Process(target=run_node, args=(node1,))
    p2 = Process(target=run_node, args=(node2,))

    #p1.start()
    #p2.start()

    t1 = threading.Thread(target=run_backend)
    t1.start()
    t1.join()

