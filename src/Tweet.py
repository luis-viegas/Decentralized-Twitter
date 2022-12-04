import json


class Tweet:
    def __init__(self, user_id, text, time):
        self.user_id = user_id
        self.text = text
        self.time = time
        
        #hash the tweet user_id + text + time
        self.tweet_id = hash(str(user_id) + text + str(time))
        
    def __eq__(self, __o: object) -> bool:
        return self.tweet_id == __o.tweet_id
    
    def to_json(self):
        return json.dumps({
            'tweet_id': self.tweet_id,
            'user_id': self.user_id,
            'text': self.text,
            'time': self.time
        })
        
        
    @staticmethod
    def from_json(json_str):
        if not json_str:
            return None
        json_obj = json.loads(json_str)
        return Tweet(json_obj['tweet_id'], json_obj['user_id'], json_obj['text'], json_obj['time'])
    
        