#Présentation du READ.ME:



Groupe de TD: BI TD02 , Groupe Projet:2 , Nom du Projet: 2048 ,
Membres du groupes Projet: Mezouer Amin , Benichou Lily-May , Dubrail Pio,
Nom de l'Enseignant : Jean Tshibangu Muabila,
URL du depot du projet:https://github.com/lilymaybenichou/2048
Documentation de l'utilisation du programme: 
LE PROGRAMME:
JEU 2048:
Le jeu du 2048 est composée de différentes parti , ici nous allons le documenter plus spécifiquement en 3 partie,La Première parties détaillera L'Interface Graphique et son utilisation , La Seconde partie 
présentera plus en détail le code et son utilisation tandis que la 3eme et dernière parti présentera 
les différentes sources utilisé pour la réalisation de ce code .
(Pour information , la documentation ici ne résume que le code dans ça globalité et seul les points 
important son abordés )

# 1ere partie l'Interface Graphique:


Pour cette Interface graphique nous avons utiliser une fenetre tkinter dans laquelle nous avons implémenter différent boutons notamment le bouton Left,Right,Up,Down et le bouton Play (les autres boutons tel que le bouton Exit,Save et Load on été rajouter dans le menu que nous détailerons plus 
tard). Les Différents boutons cité precédemment on un role majeur dans le jeux notament pour les 
déplacement par exemple . Ces differents boutons ont été crée avec des paramètres notamment au niveau 
de la couleur et de leur taille et ses boutons on été positionner au niveaux de la grille de façon a 
etre alignéé les uns a coté des autres . Nous avons aussi crée un menu qui contient différente label tel que le label pour enregistrer sous  ou encore d'autres permettant de paratger le score sur les réseaux sociaux . Ce menu est pratique car il nous a permis de mettre les différents boutons tel que le bouton 
Save,Load et Exit dans le menu permettant a l'Interface Graphique d'etre plus propre .

# 2eme partie de le Code:

Le code ici comprend différentes fonctions que nous avons utilisée,
Tout d'abord , pour la création d'une grille nous avons créé une grille 4x4 (car il y a 16 cases aux totals dans le jeu du 2048). 
La grille est d'abord nulle et on rajoute a l'interieur de cette grille 4 sous-liste avec la boucle 
for permettant de rajoute 4 sous-liste a l'interieur de la grille . 
Ensuite les 4 sous-listes sont multipliées par 0 car elle sont toute vides au debut .
Ensuite , la fonction ajoutenombre() permet quant à elle de ajouter un nombre dans la grille ,
a l'intérieur de cette fonction il y a l'utilisation de la fonction global qui permet de indiquer que la variable utiliser a l interieur de la fonction et la meme que celle utiliser a exterieur , le random randint permet l'ajout aléatoire de ici les differentes colonnes et lignes de la grille, 
la fonction ici donne grace a la fontion random randint donne 1 nombre soit un 2 ou 4 dans la grille 
ici on cherche a ce que a ce que certain endroit de la grille ne sont pas vides pour ajouter des nombres
ensuite on ajoute soit un deux ou quatre.
Après nous avons crée une fonction qui permet l'affichage de la grille , cette fonction nous est utile car elle nous permet de  d'afficher la grille le score et la fenetre qui on été pris en paramètre
Pour resumer cette fonction permet que la grille est stocker dans une variable globale et le score aussi 
 la boucle for ici permet de se promener dans la grille et verifie si la valeur et egale a zéro 
 si la ligne precedente est vrai alors il y a la creation d un label  totalement vide avec de la couleur qui est du gris si ce n'est pas le cas alors elle cree un label avec comme fond du une couleur blanche 
 et la valeur (cela est utile pour afficher la creation d'une grille avec des valeurs ),
score_label affiche le score actuel a cote du text "Score"
Ensuite il y a les différentes fonctions de mouvement pour le deplacement dans les 4 directions soit de 
déplacer a gauche a droite en haut et en bas , nous allons ici les détailler rapidement une par une pour bien comprendre leur fonctionnement :

Tout d'abord la fonction transpose bas permet de deplacer les nombres vers le bas cela ce fait du faite que ici il y a l utilisation d une double boucle soit for i in range et ensuite la boucle for j in range
Cela permet de voyager a travers les differentes cases du tableau 
 la premiere boucle for parcout les lignes de de la troisime a la premiere tandis que la deuxieme parcourt chaque colonne
si une case n est pas egal a zero et donc elle n est pas vide , la fonction cherche et trouve la premiere
 case vide et en dessous de elle et elle regarde toutes les cases en dessous de elles dans la meme colonnes
Si il y a une case vide trouver par la fonction alors alors la fonction deplace une case non vide vers
la case vide sinon elle ne fait rien 
lors de la seconde boucle imbriquée , la fonction voyage a travers chaque case et signale les cases(ici 2 cases) avec le meme nombres qui sont a coté  .  Si c est le cas alors la case qui est dessous est multiplier par deux et la case du haut est remplacer par un zero  le score augmente a la valeur de la case du bas qui est multiplier par deux A la fin , la fonction appel 2 autres fonctions soit la fonctions ici ajouter_nombre() et la fonction afficher_grille() pour mettre a jour la grille .

Ensuite , la fonction transpose haut ici cette focntion permet de deplacer tout les nombres vers le haut 
la 1ere boucle for ici parcourt les lignes de la deuxieme a la quatrieme ligne tandis que la 2eme boucle for ici parcourt chaque colonne  de la matrice  si la case contient une nombre pas egal a zero alors la fonction cherche la permiere case vide en dessus de cette case et deplace le nombre 
 la deuxieme boucle double boucle (=boucle imbriquées) for permet la verification de si deux nombres 
 sont a coté dans une colonne (car elle le deplace vers le haut et si c est le cas alors )=
il y a une addition et on deplace le resultat de l addition dans la case vide en dessous de l addition  ensuite il y a la mise a jour de la grille .

La fonction transpose gauche la fonction ici permet de deplacer les nombres vers la gauche 
 la premiere boucle for voyage a travers chaque ligne tandis que la seconde avance a travers chaque colonne de la deuxieme a la quatrieme
 si une case contient un nombre pas egal a zero alors la fonction cherchera la premiere case vide 
 a gauche de cette case et elle y  placera le nombre 
la deuxime boucle for permet la verification pour savoir si deux nombres identique sont cote a cote  si elle est verifier et vrai alors elle les additone et deplace le resulat dans la case vide 
 a gauche des deux nombres identiques cote a cote additionner 
 ensuite la fonction ajoute un nombre aleatoire a la grille , affiche la grille et met 
 a jour le score 

Enfin , la fonction transpose droite , cette fonction permet de deplacer les nombres vers la droite ,
 la premiere boucle permet a la fonction de voyager a chaque ligne tandis que la  deuxieme boucle permet
 de parcourir de la troisieme a la premiere colonne , si la case a un nombre qui n est pas egal a zéro 
 alors la fonction cherche la premiere case vide a droite de cette case et deplace le nombre 
la deuxieme boucle permet la verification pour savoir si deux nombres sont identiques et cote 
 a cote si c est le cas elle sont toutes les deux additionners et le resultat et deplacer dans une 
 case vide a droite 
 a la fin la fonction ajoute ensuite un nombre aleatoire et met a jour le score et affiche la nouvelle
 grille qui es mis a jour

Dernierement on affiche un score a la fin grace a score_label et score_label.grid

# Source:
- Pour le changement des couleurs des différentes cases en fonctions du chiffre(nombre)
#https://medium.com/@jofre44/game-app-with-python-and-tkinter-let-s-play-2048-e9e25223a711
- Pour le background
#https://www.wikipython.com/tkinter-ttk-tix/summary-information/colors/



 

