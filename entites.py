class Entity:
    def __init__(self,name,hp,defense,attack):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.atack = attack
        self.hpmax = hp   
        
    def is_alive(self):
        if self.hp > 0:
            return  True
        return False
    
    def take_damage(self,atack,defense):
        domage = atack - defense
        if domage < 0:
            domage = 0
        return domage
            
    def heal(self,heal_pv):
        self.hp=self.hp+heal_pv
        if self.hp > self.hpmax:
            self.hp = self.hpmax
        return self.hp
    
    def attack(self,domage,hp):
        self.hp = hp - domage
        if self.hp < 0:
            self.hp = 0
        return self.hp
    def play_turn(self,cible):
        attack = cible.attack
        return attack
    
    def __str__(self,name,hp,atack,defense,hpmax):
        return f"{self.name}  {self.hp}\{self.hpmax},{self.atack},{self.defense}"

  