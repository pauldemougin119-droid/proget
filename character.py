from entites import *

class Character(Entity):
    def __init__(self,liste_items):
        super().__init__()
        self.equipement = []
      
    @property  
    def attack(self,item,attack):
        take_damage = attack + item.effect
        return take_damage     
    
    @property
    def defense(self,item,defense):
        take_defense = defense + item.effect
        return take_defense

    def equiper_items(self,items,equipement): 
        self.equipement.append(items)
        return self.equipement
    
    def desquiper_items(self,items,equipement):
        self.equipement.remove(items)
        return self.equipement
    
    def Is_slot_available(self,equipement,slot_name):
        for item in equipement:
            if item.name == slot_name:
                return True
        return False
    
    def get_equipement(self,slot_name,equipement):
        for item in equipement:
            if item.name == slot_name:
                return item
    def project_dammage(self,liste_monsters):
        choix_cible = input("Choisissez une cible : ")
        cible=liste_monsters[int(choix_cible)-1]
        self.take_damage(self.attack, cible.defense)
        self.attack(cible.take_damage, cible.hp)
        return cible.hp
        
   
        