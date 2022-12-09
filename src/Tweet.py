import json
import time
import rsa

class Tweet:
    def __init__(self, username, text, time, tweet_id = None):
        self.username = username
        self.text = text
        # Time is taken in seconds to allow a sort of the list of tweets
        self.time = time
        
        #hash the tweet user_id + text + time
        self.tweet_id = tweet_id if tweet_id is not None else hash(str(username) + text + str(time))


        
    def __eq__(self, __o: object) -> bool:
        return self.tweet_id == __o.tweet_id
    
    def __gt__(self, other):
        return self.time > other.time
    
    #One line with username and time of tweet and then the text of the tweet on the next line
    def __str__(self):
        return self.username + ": " + time.ctime(self.time) + "\n" + self.text
    
        
    def sign(self, private_key: rsa.PrivateKey):
        return rsa.sign(
            self.to_json(),
            private_key,
            'SHA-1'
        )

    def to_json(self):
        return json.dumps({
            'tweet_id': self.tweet_id,
            'username': self.username,
            'text': self.text,
            'time': self.time
        })


    def to_json_signed(self, private_key: rsa.PrivateKey):
        return json.dumps({
            'tweet_id': self.tweet_id,
            'username': self.username,
            'text': self.text,
            'time': self.time,
            'signature': self.sign(private_key).decode("utf-8") 
        })
                
        
    @staticmethod
    def from_json(json_str, public_key: rsa.PublicKey):
        if not json_str:
            return None
        json_obj = json.loads(json_str)
        tweet = Tweet(json_obj['username'], json_obj['text'], json_obj['time'], json_obj['tweet_id'])
        signature:str=json_obj['signature']

        # se não for válido dá throw de rsa.pkcs1.VerificationError
        rsa.verify(tweet.to_json(),signature.encode("utf-8"),public_key)
            
        return tweet
    
        