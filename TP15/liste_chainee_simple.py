#!/usr/bin/env python3

"""
  Programme pour tester des listes chaînées basiques
"""

from random import randint
from cellule import Cellule


def est_vide(liste):
    """
    Renvoie True ssi la liste chaînée passée en paramètre est vide
    """
    return liste==None

def insere_tete(liste,val):
    """
    Insère en tête de la liste chaînée une nouvelle cellule dont 
    la valeur est val et qui renvoie la nouvelle liste (c.a.d une
    référence vers la nouvelle cellule insérée en tête)
    """
    return Cellule(val,liste)

def insere_queue(liste,val):
    """
    Insère en queue de la liste chaînée une nouvelle cellule dont
    la valeur est val (on rappelle que dans cet exercice, on ne 
    dispose pas d'une référence vers la queue de la liste chaînée),
    et qui renvoie la nouvelle liste (attention à bien réfléchir 
    à ce que veut dire « nouvelle liste » dans le cas d'une liste 
    vide et dans celui d'une liste non-vide)
    """
    if est_vide(liste):return Cellule(val,None)
    return Cellule(liste.val,insere_queue(liste.suiv,val))

def supprime(lsc, val):
    """
    Supprime la premiere occurrence de val dans lsc (version naive sans fictif).
    La fonction renvoie la liste chaînée (éventuellement) modifiée et un booléen supp qui vaut True
    ssi il y a bien eu une suppression (c'est à dire si la liste chaînée initiale contenait au moins une
    occurrence de val).
    """
    supp = False
    if est_vide(lsc):
        pass
    elif lsc.val == val:
        lsc = lsc.suiv
        supp = True
    else:
        prec = lsc
        while prec.suiv is not None and prec.suiv.val != val:
            prec = prec.suiv
        if prec.suiv is not None:
            prec.suiv = prec.suiv.suiv
            supp = True
    return lsc, supp

def supprime_fictif(lsc, val):
    """
    utilise la technique de l'élément fictif en tête pour écrire un code équivalent à celui de supprimer 
    mais sans avoir à dissocier les cas particuliers. Autrement dit, la fonction supprimer_fictif ajoutera 
    un élément fictif en tête de liste avant de faire la suppression. Il suffira de changer l'appel à 
    supprimer en appel à supprimer_fictif dans le code de test pour vérifier votre fonction.
    """
    lsc=insere_tete(lsc,'?')
    supp,prec=False,lsc
    while prec.suiv is not None and prec.suiv.val != val:
        prec = prec.suiv
    if prec.suiv is not None:
        prec.suiv = prec.suiv.suiv
        supp = True
    return lsc.suiv,supp        

def affiche(liste):
    """
    Affiche à l'écran le contenu de la liste chaînée, par exemple sous le format 1 -> 7 -> 4 -> 3 -> FIN
    """
    if est_vide(liste):
        print('END')
    else:
        print(str(liste.val)+' -> ',end='')    
        affiche(liste.suiv)   

def main():
    """
    Fonction principale
    """
    lsc = None  # creation d'une liste simplement chaînée vide
    print("Liste chaînée initiale vide : ", end="")
    affiche(lsc)
    print("est vide =", est_vide(lsc))
    for _ in range(10):
        ins_en_tete = randint(0, 1) == 1
        val = randint(0, 5)
        if ins_en_tete:
            print(f"Insertion en tête de {val}  : ", end="")
            lsc = insere_tete(lsc, val)
        else:
            print(f"Insertion en queue de {val} : ", end="")
            lsc = insere_queue(lsc, val)
        affiche(lsc)
    print("est vide =", est_vide(lsc))
    print("\nListe initiale   : ", end="")
    affiche(lsc)
    while not est_vide(lsc):
        val = randint(0, 5)
        print(f"Suppression de {val} : ", end="")
        lsc, supp = supprime(lsc, val)
        if supp:
            affiche(lsc)
        else:
            print("valeur absente")


main()