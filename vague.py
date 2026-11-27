from enemy  import Enemy
from character import Character

class Vague:
    def __init__(self, list_monsters):
        self.list_monsters = list_monsters
        self.vague_actuel=0
        
        
    def get_dificulty(self, vague_actuel):
        if vague_actuel> 1 and vague_actuel< 5:
            difficulty = 1
            return difficulty
        elif vague_actuel> 5 and vague_actuel< 10:
            difficulty = 2
            return difficulty
        elif vague_actuel> 10 :
            difficulty = 3
            return difficulty
    
    def pick_enemy(self, list_monsters):
        #display_vue(vue_choix_cible)
        choix_enemy= input("Choisissez un ennemi à combattre : ")
        return choix_enemy
        
    def play_vague(self,team,choix_enemy):
        while choix_enemy.is_alive()==True:
            for character in team:
                #displya_vue(vue_info_tour)
                character.attack(choix_enemy)
            choix_enemy.attack(team)
        self.vague_actuel += 1
        return self.vague_actuel #display_vue()
            
        