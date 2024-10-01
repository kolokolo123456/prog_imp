#!/usr/bin/env python3

class Cellule_simple:

    def __init__(self,valeur,suivant):
        self.valeur=valeur
        self.suivant=suivant

    def __str__(self):
        return str(self.valeur)+' -> '
    
class Cellule_double:

    def __init__(self,valeur,precedent,suivant):
        self.valeur=valeur
        self.precedent=precedent
        self.suivant=suivant

    def __str__(self):
        return str(self.valeur)+' <-> '

class ListeSimplementChainee:

    def __init__(self,tete):
        self.tete=tete

    def ajoute_tete(self,valeur):
        self.tete=Cellule_simple(valeur,self.tete)    

    def affiche(self):
        cell=self.tete
        while cell!=None:
            print(cell,end='')
            cell=cell.suivant
        print("END")

    def supprime_queue(self):
        if self.tete!=None:
            if cell.tete.suivant==None:
                cell.tete=None
            else:    
                cell=self.tete
                while cell.suivant.suivant!=None:
                    cell=cell.suivant
                cell.suivant=None

class ListeDoublementChainee:

    def __init__(self):
        self.tete=Cellule_double('?',None,None)
        self.queue=Cellule_double('!',None,None)
        self.tete.suivant=self.queue
        self.queue.precedent=self.tete

    def ajoute_tete(self,valeur):
        self.tete.suivant=Cellule_double(valeur,self.tete,self.tete.suivant)
        self.tete.suivant.suivant.precedent=self.tete.suivant

    def affiche(self):
        print('TETE',end='')
        cell=self.tete
        while cell.suivant!=None:
            print(cell,end='')
            cell=cell.suivant
        print('QUEUE')

    def supprime_queue(self):
        if self.tete.suivant.suivant!=None:
            self.queue.precedent.precedent.suivant=self.queue
            self.queue.precedent=self.queue.precedent.precedent



                            