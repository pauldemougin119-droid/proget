from entites import *

class Character(Entity):
    def __init__(self,liste_items):
        super().__init__()
        self.equipement = []
      
    @property  
    
    
    
    
        
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
        return self.equipement