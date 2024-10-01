#!/usr/bin/env python3
"""
  Tableaux d'entiers
"""

from random import randint

# TODO : implantez les fonctions :
#  - cree
#  - indice_prem_occ
#  - echange
#  - inverse
#  - min_et_max

def cree(taille):
    return [randint(1,9) for _ in range(taille)]

def indice_prem_occ(tab,val):
    for i in range(len(tab)):
        if tab[i]==val:return i
    return -1

def echange(tab, idx1, idx2):
    tab[idx1],tab[idx2]=tab[idx2],tab[idx1]

def inverse(tab):
    i,j=0,len(tab)-1
    while i<j:
        echange(tab,i,j)
        i+=1
        j-=1

def min_et_max(tab):
    if tab==[]:return (-1,-1)
    min,max=0,0
    for i in range(len(tab)):
        if tab[i]<tab[min]:min=i
        elif tab[i]>tab[max]:max=i                    
    return min,max
def main():
    """
    Fonction principale
    """
    for taille in range(6):
        print("-- Taille =", taille, "--")
        tab = cree(taille)
        print("Tableau initial :", tab)
        for idx in range(taille):
            print("Indice de", tab[idx], ":", indice_prem_occ(tab, tab[idx]))
        print("Indice de 10 :", indice_prem_occ(tab, 10))
        inverse(tab)
        print("Tableau inverse :", tab)
        idx_min, idx_max = min_et_max(tab)
        if idx_min == idx_max == -1:
            print("Pas de valeur min ni max dans un tableau vide !")
        else:
            print(f"Valeur minimale {tab[idx_min]} à l'indice {idx_min}")
            print(f"Valeur maximale {tab[idx_max]} à l'indice {idx_max}")
        print()


main()