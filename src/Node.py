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

    async def set(self, key, value):
        await self.server.set(key, value)

    async def get(self, key):
        return await self.server.get(key)

    async def tweet(self, text: str):
        tweet = Tweet(self.username, text, 0)
        self.user.add_tweet(tweet.tweet_id)
        # await self.set(tweet.tweet_id, tweet.to_json())
        # await self.set(self.username, self.user.to_json())
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
        self.pool.apply_async(self.update_user_DHT)
        return True

    async def unfollow(self, username: str):
        user = await self.get(username)
        if user is None:
            return False
        self.user.unsubscribe(username)
        self.pool.apply_async(self.update_user_DHT)
        return True

    
    #TODO : define these methods/ current implementation is just for testing
    async def get_timeline(self):
        print(str(self.timeline))
        return [ tweet.to_json() for tweet in self.timeline.tweets ]
     
    async def update_timeline(self):
        print("maia")
        self.timeline.update()
        print("maia2")
        
        for user in self.user.following:
            print(user)
            user_pk = self.user.following_pk[user]
            print(user_pk)
            user = await self.get(user)
            if(user is None):
                continue
            print("maia3")
            print(user)
            user = User.from_json(user, user_pk)
            print("maia4")
            for tweet in user.tweets:
                #Check if any tweet in timeline has the same id as the tweet in user.tweets
                if tweet in [tweet.tweet_id for tweet in self.timeline.tweets]:
                    continue
                print("maia8")
                tweet = await self.get(tweet)
                tweet = Tweet.from_json(tweet,user_pk)
                print("maia9")
                self.timeline.add_tweet(tweet)
                
        
    
    # Updates user timeline every n seconds (Used by ThreadPool)
    def update_timeline_thread(self, n):
        while True:
            print(self.username + " timeline updater started")
            print(self.user.following)
            time.sleep(n)
            asyncio.run(self.update_timeline())
            
                
    '''
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
        '''

    async def get_following(self):
        return self.user.following
    
    async def get_user(self, username: str):
        return username




    # Used for testing and hard coded scenarios
    async def hard_coded_tweet(self, text: str):
        tweet = Tweet(self.username, text, time.time())
        self.user.add_tweet(tweet.tweet_id)
        self.timeline.add_tweet(tweet)
        await self.set(self.username, self.user.to_json_signed(self.private_key))
        await self.set(tweet.tweet_id, tweet.to_json_signed(self.private_key))
        
        
    async def hard_coded_follow(self, username: str):
        user = await self.get(username)
        if user is None:
            return False
        self.user.subscribe(username)
        await self.set(self.username, self.user.to_json_signed(self.private_key))
        return True
        
        
        


    async def run(self):

        await self.init_server()

        # TODO : get user from authentication
        while self.username is None:
            await asyncio.sleep(1)
            #print("waiting for login")

        user = User(self.username, self.node_ip, self.node_port)
        self.user = user
        self.timeline = Timeline(self.user, []) 
        #Check if user already exists
        user_DHT = await self.get(self.username)
        if(user_DHT is None):
            await self.set(self.username, user.to_json())
        else:
            self.user = User.from_json(user)
            for tweet in self.user.tweets:
                tweet = await self.get(tweet)
                self.timeline.add_tweet(Tweet.from_json(tweet))
                
        self.pool = ThreadPool()

        if self.node_id == 1:
            self.pool.apply_async(self.update_timeline_thread, (3,))
        
        if self.node_id == 2:
            await self.hard_coded_tweet("Hello World")
            await self.hard_coded_tweet("Hello World 2")
        
        if self.node_id == 3:
            time.sleep(3)
            #await self.hard_coded_follow("node3")
            await self.hard_coded_tweet("Hello World 3")
            
            
        while True:
            await asyncio.sleep(3)
                
                
                


                
                
                
                
                
                
                



