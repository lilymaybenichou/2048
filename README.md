#Présentation du READ.ME:



Groupe de TD: BI TD02 , Groupe Projet:2 , Nom du Projet: 2048 ,
Membres du groupes Projet: Mezouer Amin , Benichou Lily-May , Dubrail Pio,
Nom de l'Enseignant : Jean Tshibangu Muabila,
URL du depot du projet:https://github.com/lilymaybenichou/2048
Documentation de l'utilisation du programme: 
LE PROGRAMME:
JEU 2048:
Le jeu du 2048 est composée de différentes parties , ici nous allons le documenter plus spécifiquement en 3 parties,La Première Parties détaillera L'Interface Graphique et son Utilisation , La Seconde Parties 
présentera plus en détail le code et son utilisation tandis que la 3eme et dernière Parti présentera 
les différentes sources utilisé pour la réalisation de ce code .
(Pour information , la documentation ici ne résume que le code dans ça globalité et seul les points 
important son abordés )

# 1ere partie l'Interface Graphique:

Pour cette Interface Graphique nous avons utiliser une Fenetre Tkinter dans laquelle nous avons implémenter différents boutons notamment le bouton Left,Right,Up,Down et le Bouton Play (les autres Boutons tel que le Bouton Exit,Save et Load on été ajouter (pour plus d'homogénéité) dans le menu que nous détaillerons plus tard.)
Les Différents Boutons cité precédemment ont un role majeur dan l'utilisation du jeux notamment pour les 
déplacement par exemple . Ces différents Boutons ont été crée avec différent caractères propres à chacun notamment au niveau de la couleur et de leur taille et ses boutons on été positionner au niveaux de la grille de façon à être alignéé les uns a coté des autres . Nous avons aussi crée un Menu qui contient différents Label tel que le Label pour Noter le jeu ou encore d'autres permettant de partager le score sur les réseaux sociaux. Ce Menu est pratique car il nous à permis de mettre les différents Boutons tel que le Bouton Save,Load et Exit dans le Menu permettant a l'Interface Graphique d'etre plus méticuleux .

# 2eme partie de le Code:

Le Code ici comprend différentes fonctions que nous avons utilisée pour le Jeux du 2048,
Tout d'abord , pour la création d'une Grille nous avons créé une Grille 4x4 (car il y a 16 cases aux totals dans le Jeu du 2048). 
La grille est d'abord nulle et on rajoute a l'intérieur de cette Grille 4 sous-liste avec la boucle 
for permettant de rajoute 4 Sous-Liste a l'intérieur de la grille. 
Ensuite les 4 sous-listes sont multipliées par 0 car elle sont toute vides au debut .
Ensuite , la Fonction ajoutenombre() permet quant à elle de ajouter un nombre dans la grille ,
a l'intérieur de cette fonction il y a l'utilisation de la fonction global qui permet de indiquer que la variable utiliser a l'interieur de la fonction et la meme que celle utiliser a exterieur , le random randint permet l'ajout aléatoire dans  ici les differentes colonnes et lignes de la grille, 
la fonction ici donne grâce a la fontion random randint donne 1 nombre soit un 2 ou 4 dans la grille 
ici on cherche a ce que a certain endroit de la grille ne sont pas vides pour ajouter des nombres
ensuite on ajoute soit un deux ou un quatre.
Après nous avons crée une fonction qui permet l'affichage de la grille , cette fonction nous est utile car elle nous permet de  d'afficher la grille le score et la fenetre qui on été pris en paramètre.
Pour resumer, cette fonction permet a ce que  la grille soit stocker dans une variable globale et le score aussi la boucle for ici permet de se promener dans la grille et verifie si la valeur et egale a zéro si la ligne prècedente est vrai alors il y a la creation d un label  totalement vide avec de la couleur qui est du gris si ce n'est pas le cas alors elle cree un label avec comme fond du une couleur blanche et la valeur (cela est utile pour afficher la creation d'une grille avec des valeurs ),
score_label affiche le score actuel a cote du text "Score"
Ensuite il y a les différentes fonctions de mouvement pour le deplacement dans les 4 directions soit de 
déplacer a gauche a droite en haut et en bas , nous allons ici les détailler rapidement une par une pour bien comprendre leur fonctionnement :

Tout d'abord la fonction transpose bas permet de deplacer les nombres vers le bas cela ce fait du faite que ici il y a l'utilisation d une double boucle soit for i in range et ensuite la boucle for j in range
Cela permet de voyager a travers les differentes cases du tableau : 
la premiere boucle for parcout les lignes  de la troisième a la première tandis que la deuxieme boucle parcourt chaque colonne,
si une case n'est pas egal a zéro et donc cette dernière n'est pas vide alors , la fonction cherche et trouve la premiere case vide et en dessous de elle et elle regarde toutes les cases en dessous de elle dans la meme colonnes
Si il y a une case vide trouver par la fonction alors alors la fonction deplace une case non vide vers
la case vide sinon elle ne fait rien. 
Lors de la seconde boucle imbriquée , la fonction voyage a travers chaque case et signale les cases(ici 2 cases) avec le meme nombres qui sont a coté  .  Si c'est le cas alors la case qui est dessous est additionné par la case du haut qui est remplacer par un zéro le score augmente à la valeur de la case du bas qui est additonnée avec la case du haut le resultat de l'addition se retrouvera tout en bas de la grille . A la fin , la fonction appel 2 autres fonctions soit la fonctions ici ajouter_nombre() et la fonction afficher_grille() pour mettre a jour la grille .

Ensuite , la fonction transpose haut ici cette fonction permet de deplacer tout les nombres vers le haut 
la 1ere boucle for ici parcourt les lignes de la deuxieme a la quatrieme ligne tandis que la 2eme boucle for ici parcourt chaque colonnes  de la matrice  si la case contient un nombre pas égal a zéro alors la fonction cherche la première case vide haut dessus de cette case et  déplace le nombre. 
La deuxieme boucle double boucle (=boucle imbriquées) for permet la vérification de si deux nombres 
sont à coté dans une colonne (car elle les additione et le déplace vers le haut et si c est le cas alors ),
il y a une addition et on déplace le résultat de l'addition dans la case vide haut dessus  ensuite il y a la mise a jour de la grille .

La fonction transpose gauche la fonction ici permet de deplacer les nombres vers la gauche,
la premiere boucle for voyage a travers chaque ligne tandis que la seconde avance a travers chaque colonne de la deuxieme a la quatrieme
si une case contient un nombre pas egal a zero alors la fonction cherchera la premiere case vide 
a gauche de cette case et elle y placera le nombre. 
La deuxime boucle for permet la vérification pour savoir si deux nombres identique sont cote a cote si c'est le cas alors  elle le vérifie et si elle est vrai alors elle les additione et déplace le résulat dans la case vide à gauche des deux nombres identiques qui sont mis cote a cote et  additionner. 
Ensuite la fonction ajoute un nombre aléatoire à la grille , affiche la grille et met 
à jour le score.

Enfin la fonction transpose droite  permet de déplacer les nombres vers la droite ,
la premiere boucle permet a la fonction de voyager a chaque ligne tandis que la  deuxieme boucle permet
de parcourir de la troisieme a la premiere colonne , si la case a un nombre qui n est pas egal a zéro 
alors la fonction cherche la premiere case vide a droite de cette case et deplace le nombre 
la deuxieme boucle permet la verification pour savoir si deux nombres sont identiques et cote  a cote si c'est le cas elle sont toutes les deux additionners et le resultat et deplacer dans une 
case vide a droite a la fin la fonction ajoute ensuite un nombre aleatoire et met a jour le score et affiche la nouvelle grille qui est mise a jour.

Dernièrement on affiche un score a la fin grace a score_label et score_label.grid

# Source:
- Pour le changement des couleurs des différentes cases en fonctions du chiffre(nombre):
#https://medium.com/@jofre44/game-app-with-python-and-tkinter-let-s-play-2048-e9e25223a711
- Pour le background:
#https://www.wikipython.com/tkinter-ttk-tix/summary-information/colors/
- La Methode After(,.destroy) permettant ici de supprimer le bouton play une fois après sont utilisation
#https://www.geeksforgeeks.org/destroy-method-in-tkinter-python/
- Pour la Réalisation de l'Interface avec les Boutons,Labels (Cours sur github): 
#https://github.com/IN200/S2-python/blob/main/cours/02_interface_graphique/02_gui.ipynb
- Documentation sur les différentes couleurs utiliser pour interface graphique :
#https://memopy.hatenadiary.jp/entry/2017/06/11/092554
- La Methode Checkbutton pour afficher des cases: 
#https://www.tutorialspoint.com/python/tk_checkbutton.htm
- La Methode webbrowser pour ouvrir un site internet (ici les réseaux sociaux):
#https://docs.python.org/3/library/webbrowser.html
- Pour la création d'un menu (aide d'une video youtube):
#https://www.youtube.com/watch?v=jGnGnro2vsk
- Pour la création de la fonction save et load:
https://www.geeksforgeeks.org/python-asksaveasfile-function-in-tkinter/

