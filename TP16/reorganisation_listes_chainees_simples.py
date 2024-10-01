#!/usr/bin/env python3
"""
  Programme pour manipuler des listes simplement chaînées basiques.
"""

from random import randint
import traceur



class Cellule:
    """
    Une cellule est composée d'une valeur et d'une référence vers la
      cellule suivante (ou None s'il n'y a pas de suivant)
    """

    # pylint: disable=too-few-public-methods

    def __init__(self, val, suiv):
        """
        Constructeur
        """
        self.val = val
        self.suiv = suiv

    def __str__(self):
        """
        Afficheur
        """
        return f"{self.val} -> "


def est_vide(lsc):
    """
    Teste si la liste chaînée est vide
    """
    return lsc is None


def insere_tete(lsc, val):
    """
    Insère une cellule de valeur val en tête de la liste chaînée
    """
    return Cellule(val, lsc)


def affiche(lsc):
    """
    Affiche la liste chaînée
    """
    cour = lsc
    while cour is not None:
        print(cour, end="")
        cour = cour.suiv
    print("FIN")


def inverse(lsc):
    """
    inverse la liste chainée
    """
    prec_prec=None
    prec=None
    while lsc!=None:
        prec_prec=prec
        prec=lsc
        lsc=lsc.suiv
        prec.suiv=prec_prec
    return prec

def insere_triee(lsc,val):
    """
    mets la valeur val dans la liste chainee lsc supposée triée dans le sens croissant
    """
    cell=lsc
    while cell!=None and cell.val<val:
        cell=cell.suiv
    cell=insere_tete(cell,val)
    return lsc    

def trie_max(lsc):
    """
    trie la liste chainée dans le sens croissant en utilisant l'algorithme
    de tri par selection.
    """
    if lsc==None or lsc.suiv==None:return lsc
    cell=lsc
    while cell.suiv!=None:
        cell_suiv=cell.suiv
        cell_max=cell_suiv
        while cell_suiv!=None:
            if cell_suiv.val<cell_max.val:
                cell_max=cell_suiv
            cell_suiv=cell_suiv.suiv
        if cell_max.val<cell.val:cell_max.val,cell.val=cell.val,cell_max.val  
        cell=cell.suiv   
    return lsc       

def init_liste_chainee(vals=None):
    """
    Initialise une liste chaînée pour tester.
    Renvoie la liste chaînée
    """
    lsc = None
    if vals is None:  # on insère 10 chiffres aléatoires
        for _ in range(10):
            lsc = insere_tete(lsc, randint(0, 9))
    else:  # on insère les valeurs passées en argument en ordre inverse
        for val in vals:
            lsc = insere_tete(lsc, val)
    return lsc

def main():
    """
    Fonction principale
    """
    print("Liste chaînée initiale  : ", end="")
    lsc = init_liste_chainee((2, 2, 4, 6, 6, 8))
    affiche(lsc)
    print("Liste chaînée inversée  : ", end="")
    lsc = inverse(lsc)
    affiche(lsc)
    print("Insertion triée : ", end="")
    for val in (1, 3, 3, 5, 7, 9, 9):
        lsc = insere_triee(lsc, val)
    affiche(lsc)
    print("Liste chaînée aléatoire : ", end="")
    lsc = init_liste_chainee()
    affiche(lsc)
    print("Tri (maximum)   : ", end="")
    lsc = trie_max(lsc)
    affiche(lsc)


main()