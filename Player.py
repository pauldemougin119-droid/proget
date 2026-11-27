from affichage import*
from vue import *
from character import*

class Player:
    def __init__(self,name,list_character,max_teams=3):
        self.name=name
        self.score = 0
        self.liste_carractere = list_character
        self.liste_inventaire = []
        self.max_teams=max_teams
          
        
        
    def create_teams(self,max_teams,liste_caractere):
        self.teams = []
        while len(self.teams)<max_teams:
            self.pick_caracter(liste_caractere,self.teams)
            ajouter=Affichage.demander_input()
            self.teams.append(liste_caractere[ajouter-1])
            
            return self.teams
    
    def pick_caracter(self,liste_carractere,teams):
        for charreter in liste_carractere:
            Character(charreter[name],charreter[hp],charreter[defense],charreter[attack])
        vue_chaarcter=Affichage.display_vue(VueSelectionEquipe(liste_carractere,teams),11)
        return vue_chaarcter
    
    
    def teams_is_alive(self,teams):
        if len(teams) != 0:
            return True
        return False

    def check_inventory(self,liste_inventaire,item):
        
        for item in liste_inventaire:
            print(f"Vous possédez l'objet : {item.name}")
            
    def use_item(self,liste_inventaire,item):
        for items in liste_inventaire:
            if items.name == item.name:
                print(f"Vous utilisez l'objet : {item.name}")
                return item.effect
         