from __future__ import annotations
import os
from abc import ABC, abstractmethod
from time import sleep
import Node

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    

# State Machine

class Console:
    _state = None
    
    def __init__(self, node: Node.Node, state: State) ->None:
        self.node = node
        self.setState(state)
            
        
    def setState(self, state):
        self._state = state
        self._state.console = self
        self._state.node = self.node
        
    def currentState(self):
        return self._state

    async def handle_state(self):
        await self._state.handle_input(self._state)
    
    
        
            


# States

class State(ABC):
    @property
    def console(self) -> Console:
        return self._console
    
    @property
    def node(self) -> Node.Node:
        return self._node

    @console.setter
    def console(self, console: Console) -> None:
        self._console = console
        
    @node.setter
    def node(self, node: Node.Node) -> None:
        self._node = node

    @abstractmethod
    async def handle_input(self) -> None:
        pass
    
    
class Home(State):
    
    async def handle_input(self):
        cls()
        
        print("Twitter Clone")
        
        print( str(await self.node.get_timeline()))
        
        print("Actions:")
        print("1. Post a tweet")
        print("2. View my tweets")
        print("3. View who I am following")
        print("4. Follow a user")
        print("5. Unfollow a user")
        print("6. Exit")
        print("Please enter a number: ", end="")
        
        action = 0
        
        while(True):
            try:
                action = int(input())
                if action < 1 or action > 6:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a number: ", end="")
                
        self.handle_action(self, action)
        
    def handle_action(self, action):
        action = str(action)
        if action == "1":
            self.console.setState(PostTweet)
        elif action == "2":
            self.console.setState(ViewMyTweets)
        elif action == "3":
            self.console.setState(ViewFollowing)
        elif action == "4":
            self.console.setState(FollowUser)
        elif action == "5":
            self.console.setState(UnfollowUser)
        elif action == "6":
            self.console.setState(Exit)
        else:
            print("Invalid action")
            self.console.setState(Home)

    
class PostTweet(State):
    
    async def handle_input(self):
        cls()
        
        print("Post a tweet")
        print("Please be aware that tweets are limited to 140 characters.")
        print("If you want to return to the home screen, enter 'exit'.")
        print("Enter your tweet: ", end="")
        
        while(True):
            try:
                tweet = input()
                if len(tweet) > 140:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a tweet: ", end="")
        
        await self.handle_action(self, tweet)
        
    async def handle_action(self, tweet):
        if(tweet == "exit"):
            print("Exiting...")
            self.console.setState(Home)
        else:
            print("Tweet posted!")
            await self.node.tweet(tweet)
            
        sleep(2)
        self.console.setState(Home)
        
        
class ViewMyTweets(State):
    
    async def handle_input(self):
        cls()
        
        print("My tweets")
        print(str(await self.node.get_user_tweets()))
        print("Press enter to return to the home screen.")
        input()
        self.console.setState(Home)

class ViewFollowing(State):
    
    async def handle_input(self):
        cls()
        
        print("Users I am following")
        print(str(await self.node.get_following()))
        print("Press enter to return to the home screen.")
        input()
        self.console.setState(Home)
        
class FollowUser(State):
    
    async def handle_input(self):
        cls()
        
        print("Follow a user")
        print("Please be aware that usernames are limited to 20 characters.")
        print("If you want to return to the home screen, enter 'exit'.")
        print("Enter the username of the user you want to follow: \n", end="")
        
        while(True):
            try:
                username = input()
                if len(username) > 20:
                    raise ValueError
                if(await self.node.get_user(username) == None):
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a username: ", end="")
        
        await self.handle_action(self, username)
        
    async def handle_action(self, username):
        if(username == "exit"):
            print("Exiting...")
        else:
            result = await self.node.follow(username)
            if result is True:
                print("User " + username + " followed!")
            else :
                print("You are already following this user!")
            
            
        sleep(2)
        self.console.setState(Home)
        
class UnfollowUser(State):
    
    async def handle_input(self):
        cls()
        
        print("Unfollow a user")
        print("Please be aware that usernames are limited to 20 characters.")
        print("If you want to return to the home screen, enter 'exit'.")
        print("Enter the username of the user you want to unfollow: ", end="")
        
        while(True):
            try:
                username = input()
                if len(username) > 20:
                    raise ValueError
                if(await self.node.get_user(username) == None):
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a username: ", end="")
        
        self.handle_action(self, username)
        
    async def handle_action(self, username):
        if(username == "exit"):
            print("Exiting...")
        else:
            result = await self.node.unfollow(username)
            if(result is True):
                print("User" + username + "unfollowed!")
            else:
                print("You are not following this user!")
            
        sleep(2)
        self.console.setState(Home)
        
class Exit(State):
    
    async def handle_input(self):
        cls()
        
        print("Exiting...")
        exit()
        

        
    # The common state interface for all the states

        

        
    
        
    