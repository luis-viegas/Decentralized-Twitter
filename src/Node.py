import asyncio
from kademlia.network import Server
from config import NODE_PORT, ORIGIN_IP, ORIGIN_PORT, FLASK_PORT
from multiprocessing.pool import ThreadPool

import time
import rsa

from Tweet import Tweet
from User import User
from Timeline import Timeline

class Node:
    def __init__(self, node_id: int, username: str = None, private_key: rsa.PrivateKey=None, node_ip: str = "127.0.0.1"):
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
        
    #* this function is called when the user logs in
    #* it checks if the user already exists in the DHT and if not it adds it
    async def login(self, username:str, private_key: rsa.PrivateKey):
        self.username = username
        self.private_key = private_key
        user = User(self.username, self.node_ip, self.node_port)
        self.user = user
        self.timeline = Timeline(self.user, []) 
        #Check if user already exists
        user_DHT = await self.get(self.username)
        
        if(user_DHT is None):
            #! Change later (it is here because of the hardcoded nodes)
            if(self.node_id == 2 or self.node_id == 3):
                await self.set(self.username, self.user.to_json_signed(self.private_key))
            else:
                self.pool.apply_async(self.update_user_DHT)
        else:
            self.user = User.from_json(user)
            for tweet in self.user.tweets:
                tweet = await self.get(tweet)
                self.timeline.add_tweet(Tweet.from_json(tweet))
                
    def logout(self):
        self.user = None
        self.timeline = None
        self.username = None
        self.private_key = None
    

    async def set(self, key, value):
        await self.server.set(key, value)

    async def get(self, key):
        return await self.server.get(key)

    async def tweet(self, text: str):
        tweet = Tweet(self.username, text, 0)
        self.user.add_tweet(tweet.tweet_id)
        self.timeline.add_tweet(tweet)
        self.pool.apply_async(self.update_user_DHT)
        self.pool.apply_async(self.update_tweet_DHT, (tweet,))
        
    def update_user_DHT(self):
        print("update_user_DHT")
        asyncio.run(self.set(self.username, self.user.to_json_signed(self.private_key)))
        
    def update_tweet_DHT(self, tweet: Tweet):
        asyncio.run(self.set(tweet.tweet_id, tweet.to_json_signed(self.private_key)))
        
        
    async def follow(self, username: str):
        user = await self.get(username)
        if user is None:
            return False
        if(self.user.subscribe(username)==False):
            return False
        self.timeline.update()
        self.pool.apply_async(self.update_user_DHT)
        return True

    async def unfollow(self, username: str):
        user = await self.get(username)
        if user is None:
            return False
        self.user.unsubscribe(username)
        self.timeline.update()
        self.pool.apply_async(self.update_user_DHT)
        return True

    
    async def get_timeline(self):
        print(str(self.timeline))
        return [ tweet.to_json() for tweet in self.timeline.tweets ]
     
    async def update_timeline(self):
        #If timeline is None, dont do nothing
        if(self.timeline is None):
            return
        
        for user in self.user.following:
            user_pk = self.user.following_pk[user]
            user = await self.get(user)
            if(user is None):
                continue
            user = User.from_json(user, user_pk)
            for tweet in user.tweets:
                #Check if any tweet in timeline has the same id as the tweet in user.tweets
                if tweet in [tweet.tweet_id for tweet in self.timeline.tweets]:
                    continue
                tweet = await self.get(tweet)
                tweet = Tweet.from_json(tweet,user_pk)
                self.timeline.add_tweet(tweet)
            

    async def get_following(self):
        return self.user.following
    
        #* Updates user timeline every n seconds (Used by ThreadPool)
    def update_timeline_thread(self, n):
        while True:
            time.sleep(n)
            asyncio.run(self.update_timeline())
    
    async def get_user(self, username: str):
        return username

    #* Used for testing and hard coded scenarios
    async def hard_coded_tweet(self, text: str):
        tweet = Tweet(self.username, text, time.time())
        self.user.add_tweet(tweet.tweet_id)
        self.timeline.add_tweet(tweet)
        await self.set(self.username, self.user.to_json_signed(self.private_key))
        await self.set(tweet.tweet_id, tweet.to_json_signed(self.private_key))
    

    async def run(self):


        await self.init_server()
        
        self.pool = ThreadPool()

        while self.username is None:
            await asyncio.sleep(1)
            
        if(self.node_id == 2 or self.node_id == 3):
            await self.login(self.username, self.private_key)
                

        if self.node_id == 1:
            self.pool.apply_async(self.update_timeline_thread, (3,))
        
        if self.node_id == 2:
            await self.hard_coded_tweet("Hello World")
            await self.hard_coded_tweet("Hello World 2")
        
        if self.node_id == 3:
            time.sleep(3)
            await self.hard_coded_tweet("Hello World 3")
            
        while True:
            await asyncio.sleep(3)
            if __name__ == '__main__':
                print("i am alive")
                
                
                


                
                
                
                
                
                
                



