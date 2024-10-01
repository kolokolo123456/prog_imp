#!/usr/bin/env python3


class Cellule:

    def __init__(self,valeur,precedent,suivant):
        self.val=valeur
        self.prec=precedent
        self.suiv=suivant

    def __str__(self):
        return str(self.val)+' <-> '
    
class ListeDouble:

    def __init__(self):
        self.tete=Cellule('?',None,None)
        self.queue=Cellule('!',None,None)
        self.tete.suiv=self.queue
        self.queue.prec=self.tete

    def remplir(self,tab):
        for val in tab:
            self.queue.suiv=Cellule('!',self.queue,None)
            self.queue.val=val
            self.queue=self.queue.suiv

    def afficher(self, inv=False):
        if not inv:
            print('Tete <-> ',end='')
            if self.tete.suiv!=None:  
                cell=self.tete.suiv
                while cell.suiv!=None:
                    print(cell,end='')  
                    cell=cell.suiv
            print("Queue")
        else:
            print('Queue <-> ',end='')
            if self.queue.prec!=None:  
                cell=self.queue.prec
                while cell.prec!=None:
                    print(cell,end='')  
                    cell=cell.prec
            print("Tete")

    def echanger(cell): #cell n'est pas la dernière cellule
        cell_suiv=cell.suiv
        cell.suiv=cell.suiv.suiv
        cell.suiv.prec=cell
        cell.prec.suiv=Cellule(cell_suiv.val,cell.prec,cell)
        cell.prec=cell.prec.suiv
        return cell_suiv

    def trier(self):
        if self.tete.suiv.suiv!=None and self.tete.suiv.suiv.suiv!=None:
            cell=self.tete.suiv
            while cell.suiv.suiv!=None:
                if cell.val<=cell.suiv.val:
                    cell=cell.suiv
                else:
                    ListeDouble.echanger(cell)
                    if cell.prec.prec.prec!=None:
                        cell=cell.prec.prec

from random import randint

def main():
    """
      Fonction principale
    """
    liste = ListeDouble()
    liste.remplir([randint(0, 9) for _ in range(5)])
    print("Liste initiale  : ", end="")
    liste.afficher()
    print("en sens inverse : ", end="")
    liste.afficher(True)
    cell = liste.tete.suiv
    while cell is not liste.queue.prec:
        ListeDouble.echanger(cell)
        print("Test echanger   : ", end="")
        liste.afficher()
    liste.trier()
    print("Liste triee     : ", end="")
    liste.afficher()
    print("en sens inverse : ", end="")
    liste.afficher(True)

main()                        






            



