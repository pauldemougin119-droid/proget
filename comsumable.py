from items import *

class Consomable(Items):
    def __init__(self):
        super().__init__()

    def use(self,):
        for items in self.equipement:
            if items.item_type == "consomable":
                self.equipement.pop(items)
                return items.effect