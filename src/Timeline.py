from User import User
from Tweet import Tweet

import time


class Timeline:
    def __init__(self, user: User ,tweets: list):
        self.user = user
        self.tweets = tweets
        
        self.is_valid = True
        
        for tweet in tweets:
            if tweet.username != user.username and tweet.username not in user.following:    
                self.is_valid = False
                break
            
        self.tweets.sort()
        
        
    def __eq__(self, __o: object) -> bool:
        return self.user == __o.user
    
    def __str__(self):
        timeline = "Timeline for " + self.user.username + ":\n"
        for tweet in self.tweets:
            timeline += str(tweet) + "\n"
        
        return timeline
    
    
    def add_tweet(self, tweet: Tweet):
        if tweet in self.tweets:
            return False
        
        if tweet.username != self.user.username and tweet.username not in self.user.following:
            return False
        
        if not self.is_valid:
            return False
         
        self.tweets.append(tweet)
        self.tweets.sort()
        
        
    def remove_tweet(self, tweet: Tweet):
        if(tweet not in self.tweets):
            return False
        
        self.tweets.remove(tweet)
        
        self.is_valid = True
        for tweet in self.tweets:
            if tweet.username != self.user.username and tweet.username not in self.user.following:
                self.is_valid = False
                break
            
        return self.is_valid
        
    def set_tweets(self, tweets: list):
        
        self.tweets = tweets
        self.tweets.sort()
        
        self.is_valid = True
        for tweet in self.tweets:
            if tweet.username != self.user.username and tweet.username not in self.user.following:
                self.is_valid = False
                break
        
        return self.is_valid
            
    
    
    
        
    