## Questions TD Ransomware

# Q1 : Quelle est le nom de l'algorithme de chiffrement ? Est-il robuste et pourquoi ?

Il s'agit d'un chiffrage xor. On utilise l'opérateur binaire XOR avec comme opérande le texte 
clair et la clé (les deux préalablement encodés en binaire).
La robustesse de cette algorithme dépend de la longueur de la clef utilisée. 
Pour que l'algorithme soit robuste, il est nécessaire que la clef soit :
 - De la même longueur que le document à chiffré
 - Totalement aléatoire 
 - Qu'elle ne soit jamais réutilisée
 
 # Q2 : Pourquoi ne pas hacher le sel et la clef directement ? Et avec un hmac ?
 
 # Q3 : Pourquoi il est préférable de vérifier qu'un fichier token.bin n'est pas déjà présent ?
 
 La méthode open("file",wb) permet de créer un nouveau fichier si celui n'existe pas. Cependant 
 si ce dernier existe, il l'écrase et le remplace par les nouvelles lignes. 
 Ainsi, il est préférable de vérifier qu'un fichier token.bin n'est pas déjà présent pour 
 s'assurer de ne pas perdre le token existant. 
 
 # Q4 : Comment vérifier que la clef est la bonne ?
 
 
 
 
 
 
