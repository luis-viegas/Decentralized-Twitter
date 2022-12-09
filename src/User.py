import json
import rsa

class User:
    def __init__(self, username: str,ip: str , port: int, tweets: list = [], following: list = []):
        self.ip = ip
        self.port = port
        self.username = username
        self.tweets = tweets
        self.following = following
        #self.subscribe(self.username)
        
    def __eq__(self, __o: object) -> bool:
        return self.user_id == __o.user_id

    def sign(self, private_key:rsa.PrivateKey):
        return rsa.sign(
            json.dumps({
            'username': self.username,
            'ip': self.ip,
            'port': self.port,
            'tweets': self.tweets,
            'following': self.following}),
            private_key,
            'SHA-1'
        )
    
    def __str__(self) -> str:
        return self.username
    

    def to_json(self,private_key:rsa.PrivateKey):
        return json.dumps({
            'username': self.username,
            'ip': self.ip,
            'port': self.port,
            'tweets': self.tweets,
            'following': self.following,
            'signature': self.sign(private_key).decode("utf-8") 
        })
    
    @staticmethod
    def from_json(json_str, public_key: rsa.PublicKey):
        if not json_str:
            return None
        json_obj = json.loads(json_str)
        user=User(json_obj['username'],json_obj['ip'], json_obj['port'],  json_obj['tweets'], json_obj['following'])
        signature:str=json_obj['signature']

        # se não for válido dá throw de rsa.pkcs1.VerificationError
        rsa.verify(user.to_json(),signature.encode("utf-8"),public_key)
            
        return user
    
    
    def subscribe(self, username: str):
        if username in self.following or username == self.username:
            return False
        
        self.following.append(username)
        return True
    
    def unsubscribe(self, username: str):
        if username not in self.following or username == self.username:
            return False
        
        self.following.remove(username)
        return True

    def add_tweet(self, tweet_id: int):
        self.tweets.append(tweet_id)
    
    
    
    
        