# ce fichier python recoit des commandes depuis le cloud et va donc créer les objets demandés

# on fait un get et on recoit des commandes en reponse

	# si la commande est une gateway avec des parametres, alors il crée un objet gateway et lui set ses parametres
	# à ce moment là, la gateway existe où non: à la creation on auto rempli avec la database
	# on crée la commande
	# puis on se connecte au servers connector et on envoit la commande

	# si la commande est une app avec des parametres, alors il crée un objet app et lui set ses parametres
	# à ce moment là, l'app existe où non: à la creation on auto rempli avec la database
	# on crée la commande
	# puis on se connecte au servers connector et on envoit la commande	

	# si la commande est un mote avec des parametres, alors il crée un objet mote et lui set ses parametres
	# à ce moment là, le mote existe où non: à la creation on auto rempli avec la database
	# on crée la commande
	# puis on se connecte au servers connector et on envoit la commande	

	# si la commande demande un stream alors on en crée un avec les parametres de la commande
	# /!\ le stream prend en parametre le nombre de fois qu'il doit iteré, la frequence, et l'address et le mask du reseau de capteur qu'on demande /!\
	# on crée un thread qui va prendre le stream en arg et qui va faire des requete grace au fonctions de database
		# à chaque iteration il recupere le journal dans la database
		# on met les informations dans le bon format
		# on post les information sur l'url du cloud
	# lorsque le nombre d'iterations est passé, on supprime le thread

	# si la commande est un snap on crée banalement un snap... bref !
	# le truc qui change avec le strean est que cette fois on iterera qu'une seule fois et que la commande sql ne nous fait pas recuperer le dernier paquet d'une plage de device mais nous fait recuperer les X plus recents paquets à un certain temps donné
	# twoot..