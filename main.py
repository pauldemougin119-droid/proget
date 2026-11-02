#Connection a la base mongo db
#je me connecter sur le por de l'aplication
#je recuper la bibliotheque
#je recuper la colection personnage
# je transforme la colection en liste



#afficher le menu
    #1 aficher le score
    #2 lancer une partie
    #3 quiter le jeu
#recuper le choix du Joueur(menu)
#tanque le choix n'est pas valide (c'est un entier et que le nombre soit compri entre le min=1 et le max=3)
    #si le nombre est un entier
        #si le nombre est comprise entre le min(1) et le max(3)   
#si le choix est egale a 1  
    #1 aficher le score
#si le choix est egale a 2
    #2 lancer une partie
    #réinitialiser le score a 0
    #recuper le nom du joueur
    #cree une equipe
        #tanque l'equipe n'est pas  valide (si l'equipe est egale au max)
            #afficher la liste des personnage
            #recuper le choix du joueur (personnage)
            # ajouter un personnage valide à l'equipe
                #tanque le personnge n'est pas valide
                    #le personnage est en str
                    # il doit constituer la liste si desous
                    #afficher la liste des personnage
            
        #choisir a aléatoirement 1 monstre
        #tanque les personnage de l'equipe on leur pv valide
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
            #ajouter le score
            #afficher un message :"c'est au tour du monstre de jouer"
            
                
        #affiche le score  avec le nom du joueur
        #enregistre le score dans mongodb
            
    
# sinon
#3 quiter le jeu
