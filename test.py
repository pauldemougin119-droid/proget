from pymongo import MongoClient
#Connection a la base mongo db
#je me connecter sur le por de l'aplication
client=MongoClient("localhost",27017)
#je recuper la bibliotheque
db=client["jeu"]
#je recuper la colection personnage
collection=db["personage"]

    