import json
import time as tm
import rsa

class Tweet:
    def __init__(self, username, text, time, tweet_id = None):
        self.username = username
        self.text = text
        # Time is taken in seconds to allow a sort of the list of tweets
        self.time = time
        self.time_secs = tm.mktime(time)
        self.verified = True
        #hash the tweet user_id + text + time
        self.tweet_id = tweet_id if tweet_id is not None else hash(str(username) + text + str(time))


        
    def __eq__(self, __o: object) -> bool:
        return self.tweet_id == __o.tweet_id
    
    def __gt__(self, other):
        return self.time_secs < other.time_secs
    
    #One line with username and time of tweet and then the text of the tweet on the next line
    def __str__(self):
        return self.username + ": " + tm.ctime(self.time) + "\n" + self.text
    
        
    def sign(self, private_key: rsa.PrivateKey):
        return rsa.sign(
            self.to_json().encode(),
            private_key,
            'SHA-1'
        )

    def to_json(self):
        return json.dumps({
            'tweet_id': self.tweet_id,
            'username': self.username,
            'text': self.text,
            'time': self.time,
            'time_secs': self.time_secs
        })


    def to_json_signed(self, private_key: rsa.PrivateKey):
        return json.dumps({
            'tweet_id': self.tweet_id,
            'username': self.username,
            'text': self.text,
            'time': self.time,
            'time_secs': self.time_secs,
            'signature': self.sign(private_key).hex() 
        })
                
        
    @staticmethod
    def from_json(json_str, public_key: rsa.PublicKey):
        if not json_str:
            return None
        json_obj = json.loads(json_str)
        tweet = Tweet(json_obj['username'], json_obj['text'], tm.localtime(json_obj['time_secs']), json_obj['tweet_id'])
        signature=json_obj['signature']

        # se não for válido dá throw de rsa.pkcs1.VerificationError
        try:
            rsa.verify(tweet.to_json().encode(),bytes.fromhex(signature),public_key)
        except rsa.VerificationError:
            tweet.verified=False

            
        return tweet
    
        