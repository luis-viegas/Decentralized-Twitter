import json
import time

class Tweet:
    def __init__(self, username, text, time):
        self.username = username
        self.text = text
        # Time is taken in seconds to allow a sort of the list of tweets
        self.time = time
        
        #hash the tweet user_id + text + time
        self.tweet_id = hash(str(username) + text + str(time))
        
    def __eq__(self, __o: object) -> bool:
        return self.tweet_id == __o.tweet_id
    
    def __gt__(self, other):
        return self.time > other.time
    
    #One line with username and time of tweet and then the text of the tweet on the next line
    def __str__(self):
        return self.username + ": " + time.ctime(self.time) + "\n" + self.text
    
        
        
    
    def to_json(self):
        return json.dumps({
            'tweet_id': self.tweet_id,
            'username': self.username,
            'text': self.text,
            'time': self.time
        })
                
        
    @staticmethod
    def from_json(json_str):
        if not json_str:
            return None
        json_obj = json.loads(json_str)
        return Tweet(json_obj['tweet_id'], json_obj['username'], json_obj['text'], json_obj['time'])
    
        