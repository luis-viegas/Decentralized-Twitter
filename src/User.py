import json


class User:
    def __init__(self, user_id: int, ip: str , port: int , username: str, tweets: list, following: list):
        self.user_id = user_id
        self.ip = ip
        self.port = port
        self.username = username
        self.tweets = tweets
        self.following = following
        
    def __eq__(self, __o: object) -> bool:
        return self.user_id == __o.user_id
    
    def to_json(self):
        return json.dumps({
            'user_id': self.user_id,
            'ip': self.ip,
            'port': self.port,
            'username': self.username,
            'tweets': self.tweets,
            'following': self.following
        })
        
    def from_json(json_str):
        if not json_str:
            return None
        json_obj = json.loads(json_str)
        return User(json_obj['user_id'], json_obj['ip'], json_obj['port'], json_obj['username'], json_obj['tweets'], json_obj['following'])
    
    
        