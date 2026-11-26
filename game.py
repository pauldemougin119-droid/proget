import os
import pymongo


class Game:
    def __init__(self,player):
        self.player = player
        self.client= pymongo.MongoClient(os.getenv("localhost:27017"))
        db = self.client["game_db"]
        collection = db["games"]  
        
    def save_game(self,player,score,teams,collection):
        save_data={
            "player_name": player.name,
            "score": score,
            "teams": teams
        }
        collection.insert_one(save_data)
        
    def load_game(self,player,collection):
        for save in collection.find():
            if save["player_name"] == player.name:
                return save
        return None
    def launch_game(self):
        choix_joueur=input("choisissez un psedo ")
        lancer_game=Game(choix_joueur)
        
    def show_leaderboard(self,collection):
        leaderboard=collection.find()
        for player in leaderboard:
            print(f"Player: {player['player_name']}, Score: {player['score']},teams: {player['teams']}")
    def exit(self):
        print("Merci d'avoir joué ! À bientôt !")
        exit()