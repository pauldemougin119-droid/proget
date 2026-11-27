import os
import pymongo
from vue import *
from Player import Player
from vague import Vague




class Game:
    def __init__(self):
        
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
        choix_joueur=input("donner votre psedo :")
        joueur=Player(choix_joueur,recuperer_persos_db)
        joueur.pick_caracter(recuperer_persos_db)
        vague=Vague(recuperer_monstres_db)
        vague.pick_enemy()
        vague.play_vague()
        
    def show_leaderboard(self,collection):
        
        leaderboard=collection.find()
        for player in leaderboard:
            print(f"Player: {player['player_name']}, Score: {player['score']},teams: {player['teams']}")
    def exit(self):
        print("Merci d'avoir joué ! À bientôt !")
        exit()
        
        
def recuperer_persos_db(db):
    liste_character=list(db["characters"].find())
    return liste_character

def recuperer_monstres_db(db):
    list_monstre=list(db["monsters"].find())
    return list_monstre