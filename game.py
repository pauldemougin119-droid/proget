import os

import pymongo



class Game:
    def __init__(self,player):
        self.player = player
        self.client= pymongo.MongoClient(os.getenv("localhost:27017"))
        
    def save_game(self,player,score,teams):
        