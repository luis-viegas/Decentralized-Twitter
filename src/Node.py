import asyncio
from kademlia.network import Server
from config import NODE_PORT, ORIGIN_IP, ORIGIN_PORT
import time

from Tweet import Tweet
from User import User
import Console

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

    async def tweet(self, text: str):
        tweet = Tweet(self.username, text, time.time())
        self.user.add_tweet(tweet.tweet_id)
        await self.set(tweet.tweet_id, tweet.to_json())
        await self.set(self.username, self.user.to_json())
        
    
    #TODO : define these methods/ current implementation is just for testing
    async def get_timeline(self):
        return "timeline"
    
    async def get_user_tweets(self):
        return str(Tweet("Maia", "Hello World!", time.time()))
    
    async def get_following(self):
        return str(User("Maia", "0.0.0.0", 0,[], []))
    
    async def get_user(self, username: str):
        return username
    
    async def follow(self, username: str):
        return True
    
    async def unfollow(self, username: str):
        return True
    


    async def run(self):

        await self.init_server()

        # TODO : get user from authentication
        user = User(self.username, self.node_ip, self.node_port)
        self.user = user


        await self.set(self.username, user.to_json())


        #TEST MATERIAL
        if(self.username == "node1"):
           await self.tweet("Hello World!")

        await asyncio.sleep(5)

        if (self.username == "node2"):
            user1 = await self.get("node1")
            user1 = User.from_json(user1)
            tweet = await self.get(user1.tweets[0])
            tweet = Tweet.from_json(tweet)
            print("tweet: ", tweet.text)
        #END TEST MATERIAL

        console = Console.Console(self, Console.Home)
        while(True):
            await console.handle_state()
        

if __name__ == "__main__":
    node = Node(1, "node1")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(node.run())
    loop.close()