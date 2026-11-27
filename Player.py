
class Player:
    def __init__(self,name,recuperer_perso_db):
        self.name=name
        self.score = 0
        self.liste_carractere = recuperer_perso_db
        self.liste_inventaire = []
        max_teams=3  
        
    def create_teams(self,max_teams,pick_caracter,liste_caractere):
        self.teams = []
        for character in self.liste_carractere:
            if len(self.teams) == max_teams:
                return True
            
            return pick_caracter(liste_caractere)
    
    def pick_caracter(self,liste_carractere):    #lien avec affichage pour choisir le personnage
        #display_vue(vue_selection_equipe)
        choix = int(input("Choisissez un personnage à ajouter à votre équipe : "))
        self.teams.append(liste_carractere[choix-1])
        return self.team
    
    
    def teams_is_alive(self,teams,max_teams):
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
         