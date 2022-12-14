## Questions TD Ransomware

# Q1 : Quelle est le nom de l'algorithme de chiffrement ? Est-il robuste et pourquoi ?

Il s'agit d'un chiffrage xor. On utilise l'opérateur binaire XOR avec comme opérande le texte 
clair et la clé (les deux préalablement encodés en binaire).
La robustesse de cette algorithme dépend de la longueur de la clef utilisée. 
Pour que l'algorithme soit robuste, il est nécessaire que la clef soit :
 - De la même longueur que le document à chiffré
 - Totalement aléatoire 
 - Qu'elle ne soit jamais réutilisée

Dans ce TD, la longueur de la clef n'est pas adapté à la longueur des différents fichier .txt
et la même clef est utilisée pour chiffrer l'ensemble des fichiers.
La cible peut alors tenter de rechercher des redondances dans les fichiers chiffrés (à l'aide
d'un fichier en clair qu'elle aurait gardé sur un autre pc) et ainsi retrouver la clef.
 
 # Q2 : Pourquoi ne pas hacher le sel et la clef directement ? Et avec un hmac ?
 
 Cela permet de rendre plus compliqué les attaques 'force brute' en augmentant le temps de hachage.
 Cela va ainsi de pair avec l'utilisation de la fonction PBKDF2HMAC qui réduit volontairement la 
 vitesse des haches.
 
 # Q3 : Pourquoi il est préférable de vérifier qu'un fichier token.bin n'est pas déjà présent ?
 
 La méthode 'open("file",wb)' permet de créer un nouveau fichier si celui n'existe pas. Cependant 
 si ce dernier existe, il l'écrase et le remplace par les nouvelles lignes. 
 Ainsi, il est préférable de vérifier qu'un fichier token.bin n'est pas déjà présent pour 
 s'assurer de ne pas perdre le token existant. 
 
 # Q4 : Comment vérifier que la clef est la bonne ?
 
 Pour vérifier si la clef est la bonne, on peut réaliser une fonction check_key qui enverra la 
 clef candidate vers le CNC. On réalisera ensuite une autre fonction au niveau du CNC qui 
 comparera la clef candidate à la bonne clef (contenu dans le fichier key.bin).
 Si la clef est correct, la fonction renverra une certaine valeure qui permettra de valider
 le déchiffrement des fichiers avec cette clef.
 
 
 
 
