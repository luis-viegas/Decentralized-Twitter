import os
from abc import ABC, abstractmethod
from Node import Node
from time import sleep

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class Console:
    _state = None
    
    def __init__(self, node, state = Home):
        self.node = node
        self.setState(state)
            
        
    def setState(self, state):
        self._state = state
        self._state.console = self
        self._state.node = self
        self.handle_input()
        
    def currentState(self):
        return self._state
    
    
    def handle_input(self):
        self._state.handle_input()
        
        
    # The common state interface for all the states
class State(ABC):
    @property
    def console(self) -> Console:
        return self._console
    
    @property
    def node(self) -> Node:
        return self._node

    @console.setter
    def console(self, console: Console) -> None:
        self._console = console
        
    @node.setter
    def node(self, node: Node) -> None:
        self._node = node

    @abstractmethod
    def handle_action(self) -> None:
        pass
    
    
class Home(State):
    
    def handle_input(self):
        cls()
        
        print("Twitter Clone")
        
        print(str(self.node.get_timeline()))
        
        print("Actions:")
        print("1. Post a tweet")
        print("2. View my tweets")
        print("3. View who I am following")
        print("4. Follow a user")
        print("5. Unfollow a user")
        print("6. Exit")
        print("Please enter a number: ", end="")
        
        while(True):
            try:
                action = int(input())
                if action < 1 or action > 6:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a number: ", end="")
                
        self.handle_action(action)
        
    def handle_action(self, action):
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
    
    def handle_input(self):
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
        
        self.handle_action(tweet)
        
    def handle_action(self, tweet):
        if(tweet == "exit"):
            print("Exiting...")
            self.console.setState(Home)
        else:
            print("Tweet posted!")
            self.node.tweet(tweet)
            
        sleep(2)
        self.console.setState(Home)
        
        
class ViewMyTweets(State):
    
    def handle_input(self):
        cls()
        
        print("My tweets")
        print(str(self.node.get_my_tweets()))
        print("Press enter to return to the home screen.")
        input()
        self.console.setState(Home)

class ViewFollowing(State):
    
    def handle_input(self):
        cls()
        
        print("Users I am following")
        print(str(self.node.get_following()))
        print("Press enter to return to the home screen.")
        input()
        self.console.setState(Home)
        
class FollowUser(State):
    
    def handle_input(self):
        cls()
        
        print("Follow a user")
        print("Please be aware that usernames are limited to 20 characters.")
        print("If you want to return to the home screen, enter 'exit'.")
        print("Enter the username of the user you want to follow: ", end="")
        
        while(True):
            try:
                username = input()
                if len(username) > 20:
                    raise ValueError
                if(self.node.get_user(username) == None):
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a username: ", end="")
        
        self.handle_action(username)
        
    def handle_action(self, username):
        if(username == "exit"):
            print("Exiting...")
        else:
            self.node.follow(username)
            print("User" + username + "followed!")
            
        sleep(2)
        self.console.setState(Home)
        
class UnfollowUser(State):
    
    def handle_input(self):
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
                if(self.node.get_user(username) == None):
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a username: ", end="")
        
        self.handle_action(username)
        
    def handle_action(self, username):
        if(username == "exit"):
            print("Exiting...")
        else:
            self.node.unfollow(username)
            print("User" + username + "unfollowed!")
            
        sleep(2)
        self.console.setState(Home)
        
class Exit(State):
    
    def handle_input(self):
        cls()
        
        print("Exiting...")
        exit()
        
        
if __init__ == "__main__":
    console = Console()
        

        

            
        
        

        
    
        
    