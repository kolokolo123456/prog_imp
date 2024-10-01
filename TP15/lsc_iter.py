#!/usr/bin/env python3

"""Listes simplement chaînées + quelques operations."""


class Cellule:
    """Une cellule d'une liste."""

    def __init__(self,valeur,suivant):
        self.valeur=valeur
        self.suivant=suivant

    def __str__(self):
        return "cellule_" + str(self.valeur)


class ListeSimplementChainee:
    """Une liste simplement chaînée."""

    def __init__(self,iterable):
        if iterable==None:
            self.tete=None
            self.taille=0
        self.tete=Cellule(iterable[0],None)
        self.taille=1
        cell=self.tete
        for i in range(1,len(iterable)):
            cell.suivant=Cellule(iterable[i],None)
            self.taille+=1
            cell=cell.suivant

    def __str__(self):
        out=''
        cell=self.tete
        while cell!=None:
            out+=str(cell.valeur)+'->'
            cell=cell.suivant
        return out+'END'            



def recupere_cellules(liste_chainee):
    cell=liste_chainee.tete
    while cell!=None:
        yield cell.valeur
        cell=cell.suivant


def remplace_valeurs(liste_chainee, transforme):
    cell=liste_chainee.tete
    while cell!=None:
        cell.valeur=transforme(cell.valeur)
        cell=cell.suivant


def filtre_cellules(liste_chainee, filtre):
    if liste_chainee.tete!=None:
        cell=liste_chainee.tete
        if filtre(cell.valeur)==True:
            yield cell.valeur
        while cell.suivant!=None:
            cell=cell.suivant
            if filtre(cell.valeur)==True:yield cell.valeur

def supprime_cellules(liste_chainee, filtre):
    cells=filtre_cellules(liste_chainee,filtre)
    if cells!=None:
        while liste_chainee.tete!=None and liste_chainee.tete.valeur not in cells:
            liste_chainee.tete=liste_chainee.tete.suivant
            liste_chainee.taille-=1
        if liste_chainee.tete!=None:    
            cell=liste_chainee.tete    
            while cell.suivant!=None:
                if cell.suivant.valeur not in cells:
                    cell.suivant=cell.suivant.suivant
                    liste_chainee.taille-=1
                    cell=cell.suivant
                else:
                    cell=cell.suivant   

def concatene(liste_chainee_1, liste_chainee_2):
    if liste_chainee_1.tete==None:
        liste_chainee_1.tete=liste_chainee_2.tete
        liste_chainee_1.taille=liste_chainee_2.taille
    else:
        cell=liste_chainee_1.tete
        while cell.suivant!=None:
            cell=cell.suivant
        cell.suivant=liste_chainee_2.tete
        liste_chainee_1.taille+=liste_chainee_2.taille        
    while liste_chainee_2.tete!=None:
            liste_chainee_2.tete=liste_chainee_2.tete.suivant
            liste_chainee_2.taille-=1
           

def decoupe(liste_chainee, fonction):
    def nofonction(i):
        return not fonction(i)
    it1,it2=list(filtre_cellules(liste_chainee,fonction)),list(filtre_cellules(liste_chainee,nofonction))
    return ListeSimplementChainee(it1),ListeSimplementChainee(it2)

def f(x):
    return x**2

def pair(n):
    return n%2==0

def teste_listes():
    """On teste les operations de base, dans différentes configurations."""
    lsc1=ListeSimplementChainee(range(11))
    lsc2=ListeSimplementChainee(range(20,27))
    print("\nListe chainée initiale 1 :",lsc1)
    print("\nListe chainée initiale 2 :",lsc2)
    cells=recupere_cellules(lsc1)
    print("\nCellules de Liste chainée 1:")
    for i in cells:
        print(str(i)+' ',end='')
    print() 
    cells_even=filtre_cellules(lsc1,pair) 
    print("\nCellules pairs de Liste chainée 1:")
    for i in cells_even:
        print(str(i)+' ',end='')
    print()
    remplace_valeurs(lsc1,f)
    print("\nOn applique la fonction carré à liste chainée 1:",lsc1)
    supprime_cellules(lsc1,pair)
    print("\nOn supprime les cellules impairs de liste chainée 1:",lsc1)  
    concatene(lsc1,lsc2)
    print("\nOn concatene liste chainée 1 et liste chainée 2:")
    print("Liste chainée 1 :",lsc1)
    print("Liste chainée 2 :",lsc2)
    print("\nOn découpe liste chainée 1 en liste chainée pair et une autre impair:")
    even,odd=decoupe(lsc1,pair)
    print("Pair :",even)
    print("Impair :",odd)


    


teste_listes()
