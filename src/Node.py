import asyncio
from kademlia.network import Server
from config import NODE_PORT, ORIGIN_IP, ORIGIN_PORT, FLASK_PORT

from Tweet import Tweet
from User import User

class Node:
    def __init__(self, node_id: int, username: str = None, private_key: str=None, node_ip: str = "127.0.0.1"):
        self.server = Server()
        self.node_id = node_id
        self.username = username
        self.private_key = private_key
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

    async def tweet(self, text: str):
        tweet = Tweet(self.username, text, 0)
        self.user.add_tweet(tweet.tweet_id)
        await self.set(tweet.tweet_id, tweet.to_json_signed())
        await self.set(self.username, self.user.to_json())

    async def follow(self, username: str):
        user = await self.get(username)
        if user is None:
            return False
        self.user.subscribe(username)
        await self.set(self.username, self.user.to_json())
        return True

    async def run(self):

        await self.init_server()

        # TODO : get user from authentication
        while self.username is None:
            await asyncio.sleep(1)
            #print("waiting for login")

        user = User(self.username, self.node_ip, self.node_port)
        self.user = user
        await self.set(self.username, user.to_json())

        while True:
            await asyncio.sleep(0.1)
            #if self.username == "node1":
                #print(self.user.tweets)


