#!/usr/bin/env python3

TAILLE=5

def creer():
    """
      Crée une file de taille donnée, sous la forme de trois variables :
      - l'indice du premier (i.e. plus ancien) élément de la file ;
      - le nombre d'éléments dans la file (qu'on appellera sa taille) ;
      - le tableau contenant les valeurs, initialisé avec une valeur non-significative.
    """
    return 0, 0, ['?' for _ in range(TAILLE)]

def afficher(tab, ix_prem, taille):
    """
      Affiche le contenu de la file
    """
    print(f"(indice du premier = {ix_prem}, taille = {taille}, tableau = {tab})")

def test_inserer(tab, ix_prem, taille, vals):
    """
      Test d'insertions
    """
    print("\nJe vais faire des insertions...")
    for val in vals:
        print("Valeur à insérer :", val)
        try:
            taille = inserer(tab, ix_prem, taille, val)
        except RuntimeError as exc:
            print(exc, "=> file non modifiée")
        else:
            print("=> ", end="")
            afficher(tab, ix_prem, taille)
    return ix_prem, taille

def test_retirer(tab, ix_prem, taille, nbr):
    """
      Test de suppressions
    """
    print("\nJe vais faire des extractions...")
    for _ in range(nbr):
        try:
            ix_prem, taille, val = retirer(tab, ix_prem, taille)
        except RuntimeError as exc:
            print(exc, "=> file non modifiée")
        else:
            print(f"Valeur retirée = {val}")
            print("=> ", end="")
            afficher(tab, ix_prem, taille)
    return ix_prem, taille

def inserer(tab, ix_prem, taille, val):    
    if taille==len(tab):raise RuntimeError()
    tab[(ix_prem+taille)%len(tab)]=val
    return taille+1       

def retirer(tab, ix_prem, taille):
    if taille==0:raise RuntimeError()
    tab[ix_prem]='?'
    return (ix_prem+1)%len(tab),taille-1,tab[ix_prem]
            
def main():
    """
      Programme principal
    """
    print("Creation d'une file vide...")
    ix_prem, taille, tab = creer()
    print("=> ", end="")
    afficher(tab, ix_prem, taille)
    ix_prem, taille = test_retirer(tab, ix_prem, taille, 1)
    ix_prem, taille = test_inserer(tab, ix_prem, taille, (1, 2, 3))
    ix_prem, taille = test_retirer(tab, ix_prem, taille, 2)
    ix_prem, taille = test_inserer(tab, ix_prem, taille, (4, 5, 6, 7, 8))
    ix_prem, taille = test_retirer(tab, ix_prem, taille, 1)
    ix_prem, taille = test_inserer(tab, ix_prem, taille, (8, 9))

main()    
