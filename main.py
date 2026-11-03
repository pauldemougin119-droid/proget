#Connection a la base mongo db
#je me connecter sur le por de l'aplication
#je recuper la bibliotheque
#je recuper la colection personnage
# je transforme la colection en liste



#afficher le menu
    #1 afficher le score
    #2 lancer une partie
    #3 quiter le jeu
#demender le choix au joueur
#recuper le choix valide  du Joueur(menu)







#recuper un choix valide
#boucle 
#tant que le choix n'est pas valide 
    #si le nombre est un entier
        #si le nombre est comprise entre le min(1) et le max(3)






















   
#si le choix est egale a 1  
    #1 aficher le score
#si le choix est egale a 2
    #2 lancer une partie
    #réinitialiser le score a 0
    #demender au jouer le nom du joueur
    #recuper le nom du joueur
    #cree une equipe
        #tanque l'equipe n'est pas  valide (si l'equipe est egale au max)
            #afficher la liste des personnage
            #demender le choix au joueur
            
            #tanque le personnge n'est pas valide (le personnage est en str et doit constiteu la liste des personnage)
                #AFFICHER UN MESAGE : choix invalide choissisez un personage de la liste si dessous 
                #afficher la liste des personnage
                #demender choix du joueur      
            #recuper choix du jouer
            # ajouter un personnage valide à l'equipe

        #choisir a aléatoirement 1 monstre
        #tant que les personnage de l'equipe on leur pv valide
            
            #choisir un personage aléatoirement de l'equipe
            #affciher le message:"c'est au tour du perssonage ...(valuer au dessus) de jouer "
            #si le personager/monstre a pv valide 
                #le personage/monstre attack 
                    #pv=attacke-defence
                #afficher les statistuque du personnage /monstre
            #si pv invalide
                #afficher un mesage :"le personnage ou le monstre est mort"
            #afficher les pv
            #afficher degat recu
            #si monstre a pv invalide
                #ajouter le score
                #choisir a aléatoirement 1 monstre
            #afficher un message :"c'est au tour du monstre de jouer"
            
                
        #affiche le score  avec le nom du joueur
        #enregistre le score dans mongodb
            
    
# sinon
#3 quiter le jeu
