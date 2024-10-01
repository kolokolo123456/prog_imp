"""Module d'encodage/décodage par rotation"""


def rot(decalage, lettre):
    """Renvoie la lettre donnée encodée par rotation.

    Le décalage utilisé pour la rotation est spécifié en paramètre.
    Préconditions :
       - lettre est une chaîne de caractères de taille 1 ;
       - lettre est un soit une lettre majuscule
         soit une lettre minuscule.
    """
    # TODO
    ...
    if type(lettre)==str and type(decalage)==int and len(lettre)==1:
        if lettre.isupper():return chr((ord(lettre)-64+decalage)%26+64)
        elif lettre.islower():return chr((ord(lettre)-96+decalage)%26+96)
        return lettre


def rot13(lettre):
    """Encode la lettre donnée par rotation de 13 caractères
    (correspond au nombre de lettre du nom du TP !).

    Pour répondre à une question qui revient souvent :
    "Oui cette fonction est ultra simple, et s'implémente
    en une seule ligne".

    Préconditions :
       - lettre est une chaîne de caractères de taille 1.
    """
    # TODO
    ...
    return rot(13,lettre)
    
print(rot13('a'),rot13(':'))    
