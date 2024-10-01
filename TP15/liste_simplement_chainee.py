#!/usr/bin/env python3

"""Listes simplement chaînées + quelques operations."""

import traceur

class Cellule:
    """Une cellule d'une liste."""

    def __init__(self,valeur,suivant):
        self.valeur=valeur
        self.suivant=suivant

    def __str__(self):
        return "cellule_" + str(self.valeur)


class ListeSimplementChainee:
    """Une liste simplement chaînée."""

    def __init__(self):
        self.tete=None
        self.queue=None
        self.taille=0  


def ajoute_en_tete(liste_chainee, valeur):
    """Ajoute une cellule en tête."""
    if liste_chainee.taille==0:
        liste_chainee.tete=Cellule(valeur,None)
        liste_chainee.queue=Cellule(valeur,None)
        liste_chainee.taille=1
        pass
    liste_chainee.tete=Cellule(valeur,liste_chainee.tete)
    liste_chainee.taille+=1


def ajoute_en_queue(liste_chainee, valeur):
    """Ajoute une cellule en queue."""
    if liste_chainee.taille==0:
        liste_chainee.tete=Cellule(valeur,None)
        liste_chainee.queue=Cellule(valeur,None)
        liste_chainee.taille=1
        pass
    else:
        liste_chainee.queue.suivant=Cellule(valeur,None)
        liste_chainee.queue=liste_chainee.queue.suivant


def recherche(liste_chainee, valeur):
    """Recherche une valeur dans la liste_chainee donnée.

    Renvoie la première cellule contenant la valeur donnée ou
    None si la valeur n'est pas trouvée dans la liste_chainee.
    """
    if liste_chainee.taille==0:return None
    cell=liste_chainee.tete
    while cell.valeur!=valeur and cell.suivant!=None:
        cell=cell.suivant
    return cell   

def supprime(liste_chainee, valeur):
    """Supprime la premiere cellule contenant la valeur donnée."""
    if liste_chainee.taille==0:
        pass
    elif liste_chainee.taille==1:
        if liste_chainee.tete.valeur==valeur:
            liste_chainee.tete=None
            liste_chainee.queue=None
            liste_chainee.taille=0
    else:
        if liste_chainee.tete.valeur==valeur:
            liste_chainee.tete=liste_chainee.tete.suivant 
            liste_chainee.taille-=1
        else:
            cell=liste_chainee.tete
            while cell.suivant!=None and cell.suivant.valeur!=valeur:
                cell=cell.suivant
            if cell.suivant!=None and cell.suivant.valeur==valeur:
                if cell.suivant==liste_chainee.queue:
                    liste_chainee.queue=cell
                else:    
                    cell.suivant=cell.suivant.suivant
                     

def teste_listes():
    """On teste les operations de base, dans différentes configurations."""
    liste_chainee = ListeSimplementChainee()
    traceur.display_instance(
         liste_chainee, image_name="liste_chainee_0"
     )
    ajoute_en_tete(liste_chainee, 3)
    ajoute_en_tete(liste_chainee, 5)
    ajoute_en_tete(liste_chainee, 2)
    ajoute_en_tete(liste_chainee, 4)
    print("liste_chainee : ", liste_chainee)
    traceur.display_instance(
        liste_chainee, image_name="liste_chainee_1"
    )
    print("recherche : ", recherche(liste_chainee, 3).valeur)
    supprime(liste_chainee, 5)
    print("apres suppression de 5 : ", liste_chainee)
    traceur.display_instance(
        liste_chainee,  image_name="liste_chainee_2"
    )
    supprime(liste_chainee, 4)
    print("apres suppression de 4 : ", liste_chainee)
    traceur.display_instance(
        liste_chainee,  image_name="liste_chainee_3"
    )


teste_listes()
