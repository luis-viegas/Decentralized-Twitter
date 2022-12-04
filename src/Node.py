import asyncio
from kademlia.network import Server
from config import NODE_PORT


def start(id):
    asyncio.run(run(id))

async def run(id):
    # Create a node and start listening on port 5678
    node = Server()
    await node.listen(NODE_PORT + id)
    await node.bootstrap([("0.0.0.0", 8468)])
    
        
    # set a value for the key "my-key" on the network
    await node.set(str(id) + "oalao", "my awesome value is " + str(id))

    # get the value associated with "my-key" from the network
    result = await node.get(str(id) +  "oalao")
    print(result)
        
    while True:
        await asyncio.sleep(1)

#asyncio.run(run(1))