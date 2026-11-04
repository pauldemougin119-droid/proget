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
    #si le nombre est infèrie au min et supereieur au maximune
        #message : le choix est invalide ressiser un choix valide
        #retourne faux
    #retourne vrai


#lancement(choix)
    #si le choix est egale a 1  
        #1 afficher le score()                      <- pas encore fait
    #si le choix est egale a 2
        #2 lancer une partie()
    # sinon
        #3 quiter le jeu()

#lancer une partie()
    #demende un nom de l'utilisateur 
    #tant que il n'est valide chek equipe complet()
        #cree une equipe valide()
    #combat()

 #chek equipe complet ()
    #boucle infini
        #si la longueur de la liste de l'equipe est egale a la longueur de l'equipe
            #retouner vrai
        #message : votre equipe est incomplete
        #retourner faux       
 
#cree une equipe valide()
    #inisialise l'equipe vide
    #afficher les personage disponible()    <- on peut peut etre simplifier
    #demender personnage valide             <- avec celle la
    #tant que chek personage valide n'est pas valide()
        #affiche les personage disponible()
        #demender une personnage valide
    #ajouter personnag dans l'equipe(choix)
    #retouner l'equipe

#afficher les personnage disponible()
    #la liste des personnage disponible(db,equipe)
    #pour chaque indice dans la liste des personnage disponible
        #afficher :"i","nom", "attack", "defence" ,"pv" 
    
#la liste des personnager disponible(db,equipe)
    #transforme collection personnage en liste des personnage      <-chek fonction annex (class)
    #liste des personnage diponible=list vide
    #pour chaque perso dans la liste des personage
        #si le personage n'est pas dans l'equipe
            #ajouter le personage dans la liste des peronage disponible
        #idice des personnage disponible()
    #retouner liste des personage disponible  
       
#chek personager valide (choix,#mininume est egale au mini des personnage disponible,#maiximun est egal au maximuni des personnag disponible)
    #boucle infini      
        #si choix n' est  pas un nombre 
            # afficher message :choix invalide choissisez un personage de la liste
            #retouner faux
        #si choix<min et choix>maxi
            # afficher message :choix invalide choissisez un personage de la liste
            #retouner faux
        
   
                  
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
            