import Node
import Origin
import asyncio
import threading
import multiprocessing
from time import sleep

if __name__ == '__main__':

    #multiprocessing.Process(target=Origin.start).start()
    threading.Thread(target=Origin.run).start()

    sleep(1)

    for i in range(1,10):
        sleep(0.5)
        multiprocessing.Process(target=Node.start, args=(i,)).start()