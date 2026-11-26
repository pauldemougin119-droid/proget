class Player:
    def __init__(self,name):
        self.score = 0
        self.liste_carractere = []
        self.liste_inventaire = []
        
    max_teams=3  
        
    def create_teams(self,max_teams):
        self.teams = []
        for character in self.liste_carractere:
            if len(self.teams) == max_teams:
                return True
            
            return False
    
    def pick_caracter(self,liste_carractere,create_teams,max_teams):    #lien avec affichage pour choisir le personnage
        while create_teams(self,max_teams) == True:
            choix = int(input("Choisissez un personnage à ajouter à votre équipe (0-2) : "))
            self.teams.append(liste_carractere[choix-1])
            return self.team
        
        return self.teams
    
    
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
         