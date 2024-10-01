#!/usr/bin/env python3

from cellule import Cellule
from traceur import trace,display_instance,display_vars

@trace()
def ajoute_valeurs_cellules(cell1, cell2):
    """Renvoie la valeur de la cellule + valeur du suivant"""
    return cell1.val + cell2.val

def main():
    """Test simple du module de traçage"""
    cell42 = Cellule(42, None)
    cell41 = Cellule(41, cell42)

    somme = ajoute_valeurs_cellules(cell41, cell42)
    print("Somme des deux cellules =", somme)
    display_instance(instance=cell41)

if __name__ == "__main__":
    main()