import asyncio
from kademlia.network import Server
from config import NODE_PORT, ORIGIN_IP, ORIGIN_PORT, FLASK_PORT
import time

from Tweet import Tweet
from User import User
import Console

class Node:
    def __init__(self, node_id: int, username: str = None, node_ip: str = "127.0.0.1"):
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

    async def tweet(self, text: str):
        tweet = Tweet(self.username, text, time.time())
        self.user.add_tweet(tweet.tweet_id)
        await self.set(tweet.tweet_id, tweet.to_json())
        await self.set(self.username, self.user.to_json())

    async def follow(self, username: str):
        user = await self.get(username)
        if user is None:
            return False
        self.user.subscribe(username)
        print(self.user.following)
        await self.set(self.username, self.user.to_json())
        return True

    async def unfollow(self, username: str):
        user = await self.get(username)
        if user is None:
            return False
        self.user.unsubscribe(username)
        await self.set(self.username, self.user.to_json())
        return True

    
    #TODO : define these methods/ current implementation is just for testing
    async def get_timeline(self):
        users = self.user.following
        timeline = []
        for user in users:
            user = await self.get(user)
            user = User.from_json(user)
            for tweet in user.tweets:
                timeline.append(tweet)
        result = []
        for tweet in timeline:
            tweet_object = await self.get(tweet)
            tweet_object = Tweet.from_json(tweet_object)
            result.append(tweet_object.to_json())

        return result

    async def get_following(self):
        return str(User("Maia", "0.0.0.0", 0,[], []))
    
    async def get_user(self, username: str):
        return username


    async def run(self):

        await self.init_server()

        # TODO : get user from authentication
        while self.username is None:
            await asyncio.sleep(1)
            #print("waiting for login")

        user = User(self.username, self.node_ip, self.node_port)
        self.user = user
        await self.set(self.username, user.to_json())

        if self.username == "node2":
            await self.tweet("ola mundo!")
            await self.tweet("second tweet")
            print("posted 2 tweets")

        while True:
            await asyncio.sleep(0.1)
            if self.username == "node1":
                #print(self.user.tweets)
                result = await self.get_timeline()
                print(result)
                print(self.user.following)



