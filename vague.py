from enemy  import Monster

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
        elif vague_actuel> 10 and vague_actuel< 15:
            difficulty = 3
            return difficulty
        