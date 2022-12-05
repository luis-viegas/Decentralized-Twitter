import asyncio
from kademlia.network import Server
from config import NODE_PORT, ORIGIN_IP, ORIGIN_PORT

from Tweet import Tweet
from User import User

class Node:
    def __init__(self, node_id: int, username: str = None):
        self.server = Server()
        self.node_id = node_id
        self.username = username
        self.user = None


async def init_server(self):
    await self.server.listen(NODE_PORT + self.node_id)
    await self.server.bootstrap([(ORIGIN_IP, ORIGIN_PORT)])

async def run(self,id):

    await self.init_server()

    
    user = User(id, "0.0.0.0", NODE_PORT + id, "user" + str(id), [], [])
    tweet = Tweet(id, "tweet" + str(id), 0)
        
    # set a value for the key "my-key" on the network
    await node.set(user.username, user.to_json())
    await node.set(tweet.tweet_id, tweet.to_json())

    # get the value associated with "my-key" from the network
    result = await node.get(user.username)
    print("Got", result, "from network")
    result = await node.get(tweet.tweet_id)
    print("Got", result, "from network")
        
    while True:
        await asyncio.sleep(1)

#asyncio.run(run(1))