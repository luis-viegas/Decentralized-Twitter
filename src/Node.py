import asyncio
from kademlia.network import Server
from config import NODE_PORT, ORIGIN_IP, ORIGIN_PORT

from Tweet import Tweet
from User import User

class Node:
    def __init__(self, node_id: int, username: str = None, node_ip: str = "0.0.0.0"):
        self.server = Server()
        self.node_id = node_id
        self.username = username
        self.user = None
        self.node_ip = node_ip
        self.node_port = NODE_PORT + self.node_id


    async def init_server(self):
        await self.server.listen(self.node_port)
        await self.server.bootstrap([(ORIGIN_IP, ORIGIN_PORT)])

    async def set(self, key, value):
        await self.server.set(key, value)

    async def get(self, key):
        return await self.server.get(key)

    async def run(self):

        await self.init_server()


        user = User(self.username, self.node_ip, self.node_port)
        await self.set(self.username, user.to_json())


        #TEST MATERIAL
        if(self.username == "node1"):
            tweet = Tweet(self.username, "this is our first tweet", 0)
            await self.set("tweet.tweet_id", tweet.to_json())

        await asyncio.sleep(5)

        if (self.username == "node2"):
            result = await self.get("tweet.tweet_id")
            tweet2 = Tweet.from_json(result)
            print("tweet: ", tweet2.text)
        #END TEST MATERIAL




        while True:
            await asyncio.sleep(1)


