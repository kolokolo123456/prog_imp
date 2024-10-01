#!/usr/bin/env python3

"""
  Tris de tableaux
"""

from random import randint


def cree(taille):
    """
    Cree un tableau rempli de valeurs aléatoires
    """
    return [randint(1, 9) for _ in range(taille)]

def trie_nain(tab):
    if tab==[]:return tab
    i=0
    while i<len(tab)-1:
        if tab[i]<=tab[i+1]:i+=1
        elif tab[i]>tab[i+1]:
            tab[i],tab[i+1]=tab[i+1],tab[i]
            if i>0:i-=1
    return tab           

def recherche_min(tab, debut):
    min=debut
    for i in range(debut,len(tab)):
        if tab[min]>tab[i]:min=i
    return min 

def trie_min(tab):
    if tab==[]:return tab
    for i in range(len(tab)-1):
        min=recherche_min(tab,i)
        tab[i],tab[min]=tab[min],tab[i]
    return tab  

def decale_insere(tab, idx_val):
    val=tab[idx_val]
    while idx_val>0 and val<tab[idx_val-1]:
        idx_val-=1
    return idx_val

def trie_ins(tab):
    if tab==[]:return tab
    for i in range(1,len(tab)):
        idx=decale_insere(tab,i)
        for j in range(i,idx,-1):
            tab[j],tab[j-1]=tab[j-1],tab[j]
    return tab                     

def main():
    """
    Fonction principale
    """
    for taille in range(6):  # on teste sur des tableaux de taille 0 à 5 inclus
        print("-- Taille =", taille, "--")
        tab = cree(taille)
        tab_orig = tab[:]  # copie du CONTENU du tableau
        print("Tableau initial        :", tab)
        trie_nain(tab)
        print("Tri du nain            :", tab)
        tab = tab_orig[:]
        print("Tableau initial        :", tab)
        trie_min(tab)
        print("Tri par sélect. du min :", tab)
        tab = tab_orig[:]
        print("Tableau initial        :", tab)
        trie_ins(tab)
        print("Tri par insertion      :", tab)
        print()

main()