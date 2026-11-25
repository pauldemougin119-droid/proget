class Player:
    def __init__(self,name:str,score:int,liste_carractere,liste_inventaire):
        self.name = name
        self.score = score

        
        
    max_teams=3  
        
    def create_teams(self,liste_carractere,max_teams):
        self.liste_carractere = liste_carractere
        self.teams = []
        for i in range(0,max_teams):
            self.teams.append(self.liste_carractere[i])
        return self.teams
    def teams_is_alive(self,teams,max_teams):
        if len(teams) != 0:
            return True