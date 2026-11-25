class Player:
    def __init__(self,name:str,score:int,liste_carractere,liste_inventaire):
        self.name = name
        self.score = score
        self.liste_carractere = liste_carractere
        self.liste_inventaire = liste_inventaire
        
    max_teams=3  
        
    def create_teams(self,max_teams):
        self.teams = []
        for character in self.liste_carractere:
            if len(self.teams) == max_teams:
                return True
            
            return False
    
    def pick_caracter(self,liste_carractere,choix,create_teams,max_teams):    #lien avec affichage pour choisir le personnage
        while create_teams(self,max_teams) == True:
            #demander choix a l'utilisateur
                self.teams.append(liste_carractere[choix])
                return self.team
        
        self.teams.append(liste_carractere[choix])
        return self.teams
    
    
    def teams_is_alive(self,teams,max_teams):
        if len(teams) != 0:
            return True
        
    def check_inventory(self,liste_inventaire,item):
        if item in liste_inventaire:
            return True
        return False