from pymongo import MongoClient
#Connection a la base mongo db
#je me connecter sur le por de l'aplication
client=MongoClient("localhost",27017)
#je recuper la bibliotheque
db=client["jeu"]
#je recuper la colection personnage
collection=db["personage"]

    
    
    
#methode afficher personnage  en p(self,db)
        #liste des personnage=[]
        #pour chaque personnage dans la db
            #entiter(nom= db['nom'], est agale a  la valeur nom du diconnaire
            # pv=db['vie'], est agale a  la valeur vie du diconnaire
            # attack=db ['attack], est agale a  la valeur attack du diconnaire
            # defence=db[defence] est agale a  la valeur defence du diconnaire
            # )
            #ajouter personager dans la liste des personnage
        #retouner la liste des personnager