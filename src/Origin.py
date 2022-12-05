import asyncio
from kademlia.network import Server
from config import ORIGIN_PORT

import logging
import asyncio

from kademlia.network import Server

def run():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)


    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    log = logging.getLogger('kademlia')
    log.addHandler(handler)
    log.setLevel(logging.DEBUG)
    loop.set_debug(True)

    server = Server()
    loop.run_until_complete(server.listen(ORIGIN_PORT))

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.stop()
        loop.close()
        


if __name__ == '__main__':
    run()