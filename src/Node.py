import asyncio
from kademlia.network import Server
from config import NODE_PORT

from Tweet import Tweet
from User import User

def start(id):
    asyncio.run(run(id))

async def run(id):
    # Create a node and start listening on port 5678
    node = Server()
    await node.listen(NODE_PORT + id)
    await node.bootstrap([("0.0.0.0", 8468)])
    
    user = User("user" + str(id), "0.0.0.0", NODE_PORT + id,  [], [])
    tweet = Tweet(user.username, "tweet" + str(id), 0)
        
    # set a value for the key "my-key" on the network
    await node.set(user.username, user.to_json())
    await node.set(tweet.tweet_id, tweet.to_json())

    # get the value associated with "my-key" from the network
    result = await node.get(user.username)
    print("Got", result, "from network")
    result = await node.get(tweet.tweet_id)
    print("Got", result, "from network")
        
    while True:
        await asyncio.sleep(1)

#asyncio.run(run(1))
