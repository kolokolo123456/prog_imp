#!/usr/bin/env python3
"""
  Tableau de listes chaînées
"""

from random import randint

from cellule import Cellule

class Liste:

    def __init__(self):
        self.tete=Cellule('?')
        self.nbr_elem=0

    def __str__(self):
        k=''
        cell=self.tete.suiv
        while cell!=None:
            k+=str(cell.val)+' -> '
            cell=cell.suiv
        return k+'END'     

class TableauListe:

    def __init__(self,taille):
        self.nbr_elem=0
        self.tableauliste=[Liste() for i in range(taille)]

    def hachage(self,val):
        return val%len(self.tableauliste)

    def afficher(self):
        tab=self.tableauliste
        for i in range(len(tab)):
            print(i,tab[i],sep=':')

    def inserer(self,val):
        ind=self.hachage(val)
        self.tableauliste[ind].tete.suiv=Cellule(val,self.tableauliste[ind].tete.suiv)
        self.tableauliste[ind].nbr_elem+=1
        self.nbr_elem+=1

    def est_presente(self,val):
        ind=self.hachage(val)
        ls=self.tableauliste[ind].tete
        while ls.suiv!=None:
            if ls.suiv.val==val:return True
            ls=ls.suiv
        return False

    def supprimer(self, val):
        ind=self.hachage(val)
        ls=self.tableauliste[ind]
        cell=ls.tete
        while cell.suiv!=None and cell.suiv.val!=val:
            cell=cell.suiv
        if cell.suiv!=None and cell.suiv.val==val:
            cell.suiv=cell.suiv.suiv
            self.nbr_elem-=1
            return True
        return False


def main():
    """
    Fonction principale
    """
    struct = TableauListe(4)
    struct.afficher()
    for _ in range(10):
        val = randint(0, 9)
        print("\nAjout de la valeur", val)
        struct.inserer(val)
        struct.afficher()
    print()
    for val in range(5):
        if struct.est_presente(val):
            print(f"{val} est presente dans la structure")
        else:
            print(f"{val} est absente de la structure")
    print()
    struct.afficher()
    while struct.nbr_elem > 0:
        val = randint(0, 9)
        if struct.supprimer(val):
            print("\nSuppression de la valeur", val)
            struct.afficher()


main()
