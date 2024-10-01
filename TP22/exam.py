#!/usr/bin/env python3

import random

def echanger(tab, idx1, idx2):
    if len(tab)>1 and idx1!=idx2:
        val2=tab[idx2]
        tab[idx2]=tab[idx1]
        tab[idx1]=val2  
    
def trier_drapeau(tab):
    """
    tab[0]='j'
    """
    if len(tab)>1 and tab[0]=='j':
        id1,id2,cour=0,0,1
        while cour!=len(tab):
            if tab[cour]=='n':
                echanger(tab,cour,id2+1)
                echanger(tab,id2+1,id1)
                id1+=1
                id2+=1
            elif tab[cour]=='j':
                echanger(tab,cour,id2+1)
                id2+=1
            cour+=1   
        return (id1,id2)
    return (0,0)       

class Cellule:
    """
    Une cellule est composée d'une valeur et d'une référence vers la
    cellule suivante (ou None s'il n'y a pas de suivant)
    """
    def __init__(self, val, suiv):
        """
        Constructeur
        """
        self.val = val
        self.suiv = suiv  

def creer_liste_vide():
    """
    Renvoie une liste simplement chaînée vide.
    Elle contient en fait un élément fictif en tête (sentinelle)
    dont le champ suivant est None.
    La sentinelle a une valeur non-significative : on n'a pas le droit
    de se baser sur la valeur de cette cellule dans les fonctions
    """
    return Cellule('?', None)   

def inverser(lsc):
    if lsc and lsc.suiv:
        cell_cour=lsc.suiv
        cell_prec=None
        while cell_cour!=None:
            suiv=cell_cour.suiv
            cell_cour.suiv=cell_prec
            cell_prec=cell_cour
            cell_cour=suiv
        lsc.suiv=cell_prec

def rechercher_prec_max(lsc):
    if lsc and lsc.suiv:
        cell_max=lsc
        cell=lsc.suiv
        while cell.suiv:
            if cell.suiv.val>cell_max.suiv.val:
                cell_max=cell
            cell=cell.suiv
        return cell_max  
    return lsc    

def trier(lsc):
    res=None
    while lsc.suiv:
        cell_max=rechercher_prec_max(lsc)
        res=Cellule(cell_max.suiv.val,res)
        val=cell_max.val
        cell=lsc
        while cell.val!=val:
            cell=cell.suiv
        cell.suiv=cell.suiv.suiv
    res=Cellule('?',res)
    return res             

def ajoute_tete(lsc,val):
    return Cellule('?',Cellule(val,lsc.suiv))            

def affiche(lsc):
    cell=lsc.suiv
    while cell:
        print(str(cell.val)+' -> ',end='')
        cell=cell.suiv
    print('END')            



def test():
    tab=list(range(10))
    print(tab)
    print("On échange les éléments d'indices 5 et 7")
    echanger(tab,5,7)
    print(tab)
    tab=[random.choice(['j','n','r']) for i in range(10)]
    tab[0]='j'
    print(tab)
    print('tri tableau :')
    trier_drapeau(tab)
    print(tab)  
    lsc=creer_liste_vide()
    for i in range(10):
        lsc=ajoute_tete(lsc,i)
    affiche(lsc)    
    inverser(lsc)
    print("liste chainée inverse :")
    affiche(lsc)
    lsc=creer_liste_vide()
    for i in range(10):
        lsc=ajoute_tete(lsc,random.randint(0,10))
    affiche(lsc)
    print("max de liste chainée :")
    affiche(rechercher_prec_max(lsc)) 
    lsc=creer_liste_vide()
    for i in range(10):
        lsc=ajoute_tete(lsc,random.randint(0,10))
    affiche(lsc)
    print("tri selection :")
    lsc=trier(lsc)
    affiche(lsc)       
test()    
