#Connection a la base mongo db
#je me connecter sur le por de l'aplication
#je recuper la bibliotheque
#je recuper la colection personnage
# je transforme la colection en liste



#afficher le menu()
    #1 afficher le score
    #2 lancer une partie
    #3 quiter le jeu
    
    
#main()   
    #boucle infini
        #affiche menu() 
        #recuper un choix valide ()
        #lancement(choix)

#recuperer un choix valide(min,max)
    #boucle infini
        #demonde un choix au joueur
        #chek in choix valid()
    #convertir le choix()
    
    
#convertire le choix()
    #retourner int(choix)


#chek un choix valide(choix,min,max)
    #si le nombre n'est pas un entier
        #retourne faux
    #si le nombre est inferie au min et superei au maximune
        #retourne faux
    #retourne vraix

#lancement(choix)
    #si le choix est egale a 1  
        #1 afficher le score()
    #si le choix est egale a 2
        #2 lancer une partie()
    # sinon
        #3 quiter le jeu()

#recuper un choix valide()
    #boucle infini
        #demende un nom de l'utilisateur
        #chek nom user valide()

#chek nom use valide()
    #boncle infini
        #si le choix n'est pas un nombre
            #retourner faux
        #retourner vraix

#lancer une partie
    #recuper un choix valide()                                              <-nom du Joueur
    #cree  equipe complet()
    
#chek equipe complet ()
    #boucle infini
        #si la longuer de la liste de l'equipe est egale a 3
            #retouner vrai
        
        #retourner faux
#recuper personage db()                                             <- importe pymongo pour se coneter a la db
    #se connter a la db
    #je recuper la bibliotheque jeu
    #je recuper la colection perosnage
    
#cree une equipe compelet()
    #chek equipe complet()
    #recuper personage db()
    #transformer objet db en un objet class()                           plus tart
    #afficher personage()                                                plus tart
    #recuper personnage valide()
      
      
#demender personage au jouer()
    #boucle infini
        #input choix du joueur 
        #chek personge valide()
        
#chek personager valide (choix)
    #boucle infini      
        #si choix est un nombre
            # afficher message :choix invalide choissisez un personage de la liste
        #sinon
            #retouner vraix
                
#ajouter personnage dans l'equipe(choix)
    #inisaliser l'equipe
    #ajouter le choix dans l'equiper

#recuper personage valide()
    #demender personnager au jouer()
    #ajouter personnag dans l'equipe()
    #combat()
    
#chek equipe pv valide()
    #pour chaque personage de l"equipe
        #si chek pv valide()
            #retourner vraix
        #sinon
            #afficher message: Vous aver perdu voici le score
            #afficher score    
#chek pv valide()
    #boucle infini
        #si pv >0
            #retourner vraix
        #sinon
            #retourner faux
            #afficher un mesage :"le personnage ou le monstre est mort"    


#choisir un monstre aléatoirement()
    #importer choice


__________________________________________________________

#combat()
    #tant que chek equipe pv valide() 
        #choisir un monstre aléatoirement()  
        #lancer une vaguer() 
        #si monstre a chek valide()
            #score+1
            
   
#choisir un personage aléatoirement de l'equipe(equipe)
    #importer choice
 
 #personnage qui est en vie()
    #personnage en vie est une liste vide
    #pour chaque menbre de l'equipe
        #si persannager chek pv valide()
            #ajouter le personnage a la liste

           
            
#lancer une vaguer()
    #choisir personnage qui est en vie()
        #personage/monstre attack ()                        <- methode dans la classe principale
    #afficher les states combat()                           <- methode dans la classe

 
 
 
 _______________________________________________________________
 
    #cree une equipe
            #afficher la liste des personnage
            #tanque le personnge n'est pas valide (le personnage est en str et doit constiteu la liste des personnage)
    #combat
            
            #affciher le message:"c'est au tour du perssonage ...(valuer au dessus) de jouer "
            #afficher un message :"c'est au tour du monstre de jouer"
            
                
        #affiche le score  avec le nom du joueur
        #enregistre le score dans mongodb
            
