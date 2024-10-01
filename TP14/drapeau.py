#!/usr/bin/env python3
"""
  Pivot
"""

from random import randint

TAILLE = 20    

def drapeau(tab,idx_pivot):
    if tab==[]:return tab
    deb_piv,fin_piv,val_piv=0,0,tab[idx_pivot]
    echanger(tab,0,idx_pivot)
    for i in range(1,len(tab)):
        if tab[i]==val_piv:
            echanger(tab,i,fin_piv+1)
            fin_piv+=1
        elif tab[i]<val_piv:
            if i==fin_piv+1:echanger(tab,i,deb_piv)
            else:
                for j in range(fin_piv,deb_piv-1,-1):
                    echanger(tab,j,j+1)   
                echanger(tab,deb_piv,i)
            deb_piv+=1
            fin_piv+=1
    return deb_piv,fin_piv        

def echanger(tab, idx1, idx2):
    """
      Echange tab[idx1] et tab[idx2]
    """
    tmp = tab[idx1]
    tab[idx1] = tab[idx2]
    tab[idx2] = tmp


def main():
    """
      Fonction principale
    """
    tab = [randint(0, 10) for _ in range(TAILLE)]
    idx_pivot = randint(0, TAILLE - 1)
    print("Tableau initial :", tab)
    print("Indice du pivot : ", idx_pivot, ", valeur du pivot : ",
          tab[idx_pivot], sep="")
    print("Drapeau en place :")
    deb_piv, fin_piv = drapeau(tab, idx_pivot)
    print("  indices du pivot : de", deb_piv, "à", fin_piv)
    print("  tableau réorganisé :", tab[0:deb_piv], tab[deb_piv:fin_piv + 1], tab[fin_piv + 1:])

main()