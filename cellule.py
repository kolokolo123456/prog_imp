#!/usr/bin/env python3

"""Classe cellule pour construire des listes chainées"""

class Cellule:
    """Une cellule possède une référence vers la valeur et
    une référence vers la cellule suivante."""

    def __init__(self,valeur,suivant=None):
        self.val=valeur
        self.suiv=suivant

    def __str__(self):
        return "cellule_" + str(self.val)