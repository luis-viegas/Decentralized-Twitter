import json
import rsa
import requests

class User:
    def __init__(self, username: str,ip: str , port: int, tweets: list = [], following: list = [],following_pk: dict = {}):
        self.ip = ip
        self.port = port
        self.username = username
        self.tweets = tweets
        self.following = following
        self.following_pk = following_pk
        self.verified = True
        #self.subscribe(self.username)
        
    def __eq__(self, __o: object) -> bool:
        return self.user_id == __o.user_id

    def sign(self, private_key:rsa.PrivateKey):
        return rsa.sign(
            self.to_json(),
            private_key,
            'SHA-1'
        )
    
    def __str__(self) -> str:
        return self.username
    

    def to_json_signed(self,private_key:rsa.PrivateKey):
        return json.dumps({
            'username': self.username,
            'ip': self.ip,
            'port': self.port,
            'tweets': self.tweets,
            'following': self.following,
            'signature': self.sign(private_key).decode("utf-8") 
        })

    def to_json(self):
        return json.dumps({
            'username': self.username,
            'ip': self.ip,
            'port': self.port,
            'tweets': self.tweets,
            'following': self.following
    })

    # @staticmethod
    # def from_json(json_str):
    #     if not json_str:
    #         return None
    #     json_obj = json.loads(json_str)
    #     return User(json_obj['username'],json_obj['ip'], json_obj['port'],  json_obj['tweets'], json_obj['following'])
    
    @staticmethod
    def from_json(self,json_str, public_key: rsa.PublicKey):
        if not json_str:
            return None
        json_obj = json.loads(json_str)
        user=User(json_obj['username'],json_obj['ip'], json_obj['port'],  json_obj['tweets'], json_obj['following'])
        signature:str=json_obj['signature']

        # se não for válido dá throw de rsa.pkcs1.VerificationError
        try:
            rsa.verify(user.to_json(),signature.encode("utf-8"),public_key)
        except rsa.VerificationError:
            self.verified=False

        return user
    
    
    def subscribe(self, username: str):
        if username in self.following or username == self.username:
            print("deu falso")
            return False
        print("ola")
        self.following.append(username)
        response = requests.post('http://localhost:8000/get-public-key',json={"username":username})
        public_key_str = response.json()['response']
        self.following_pk['username'] = rsa.PublicKey.load_pkcs1(public_key_str)
        return True
    
    def unsubscribe(self, username: str):
        if username not in self.following or username == self.username:
            return False
        
        self.following.remove(username)
        return True

    def add_tweet(self, tweet_id: int):
        self.tweets.append(tweet_id)
    
    
    
    
        