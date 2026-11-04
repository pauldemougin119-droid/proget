#Connection a la base mongo db
#je me connecter sur le por de l'aplication
#je recuper la bibliotheque
#je recuper la colection personnage
# je transforme la colection en liste



#-------------------------------- Debut du jeu -------------------------
    
    
#main()   
    #boucle infini
        #affiche le menu() 
        #recuper un choix valide ()
        #lancement(choix)

#afficher le menu()
    #1 afficher le score
    #2 lancer une partie
    #3 quiter le jeu
    
    
#recuperer un choix valide(min,max)
    #demonde un choix au joueur
    #tant que ce n'est pas chek in choix valid()
        #demonde un choix au joueur
    #retourner int(choix)

#chek un choix valide(choix,min,max)
    #si le nombre n'est pas un entier
        #message : le choix est invalide ressiser un choix valide
        #retourne faux
    #si le nombre est inferie au min et superei au maximune
        #message : le choix est invalide ressiser un choix valide
        #retourne faux
    #retourne vraix


#lancement(choix)
    #si le choix est egale a 1  
        #1 afficher le score()                      <- pas encofer le score est l'affcihage du scor avd la db
    #si le choix est egale a 2
        #2 lancer une partie()
    # sinon
        #3 quiter le jeu()

#lancer une partie()
    #demende un nom de l'utilisateur 
    #tant que il n'est valide chek equipe complet()
        #cree une equipe complet()
    #combat()

 #chek equipe complet ()
    #boucle infini
        #si la longuer de la liste de l'equipe est egale a 3
            #retouner vrai
        #message : votre equipe est incomplete
        #retourner faux       

#cree une equipe compelet()                                                   
    #recuper personnage valide()
           
    
#afficher la liste des personnager disponible(db,equipe)
    #transforme les personnage en liste
    #liste des personnage diponible=list vide
    #pour chaque perso dans la liste des personage
        #si le personage n'est pas dans l'equipe
            #ajouter le personage dans la liste des peronage disponible
    #retouner la liste des personage disponible
     
#recuper personage valide()
    #inisialise l'equipe
    #afficher la liste des personage disponible(db)    <- on peut peut etre simplifier
    #demender personnage valide
    #tant que chek personage valide n'est pas valide()
        #afficher la liste des personage disponible(db)
        #demender une personnage valide
    #ajouter personnag dans l'equipe()
    #retouner l'equipe
       
#chek personager valide (choix)
    #boucle infini      
        #si choix est un nombre
            # afficher message :choix invalide choissisez un personage de la liste
            #retouner faux
        #sinon
            #retouner vraix
                
#ajouter personnage dans l'equipe(choix)
    #inisaliser l'equipe
    #ajouter le choix dans l'equiper

 #-----------------------------------------------Combat---------------------------------
 
 #combat()
    #tant que personnage est en vie()
        #choisir un monstre aléatoirement()  
        #lancer une vaguer() 
        #si monstre n' a pas chek pv valide()
            #score+1
            
 #personnage est en vie()
    #personnage en vie est une liste vide
    #pour chaque menbre de l'equipe
        #si persannager chek pv valide()
            #ajouter le personnage a la liste 
    #return 
               
#choisir un monstre aléatoirement()
    #importer choice            
                          
#chek pv valide()
    #boucle infini
        #si pv >0
            #retourner vraix
        #sinon
            #retourner faux
            #afficher un mesage :"le personnage ou le monstre est mort"       
            
#lancer une vaguer()
    #pour chaque personnage est en vie()  
        # personnage attack () 
        #afficher les states combat()
    #monstre attack()                           
    #afficher les states combat()

            
            
            
#_______________________________________________________________________                    
        #affiche le score  avec le nom du joueur
        #enregistre le score dans mongodb
            
