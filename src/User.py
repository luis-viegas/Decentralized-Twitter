import json


class User:
    def __init__(self, username: str,ip: str , port: int, tweets: list, following: list):
        self.ip = ip
        self.port = port
        self.username = username
        self.tweets = tweets
        self.following = following
        
    def __eq__(self, __o: object) -> bool:
        return self.user_id == __o.user_id
    
    def to_json(self):
        return json.dumps({
            'username': self.username,
            'ip': self.ip,
            'port': self.port,
            'tweets': self.tweets,
            'following': self.following
        })
    
    @staticmethod
    def from_json(json_str):
        if not json_str:
            return None
        json_obj = json.loads(json_str)
        return User(json_obj['username'],json_obj['ip'], json_obj['port'],  json_obj['tweets'], json_obj['following'])
    
    
    def subscribe(self, username: str):
        if username in self.following:
            return False
        
        self.following.append(username)
        return True
    
    def unsubscribe(self, username: str):
        if username not in self.following:
            return False
        
        self.following.remove(username)
        return True
    
    
    
    
        