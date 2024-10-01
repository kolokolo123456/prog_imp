#!/usr/bin/env python3
"""
Crible d'Ératosthène
"""

import math

def init_tab(taille):
    # TODO
    ...
    out=[True for i in range(taille)]
    out[0]=False
    return out

def filtre(les_premiers, prem):
    # TODO
    ...
    for i in range(prem,len(les_premiers)):
        if (i+1)%prem==0:les_premiers[i]=False  

def affiche(les_premiers, val_max):
    # TODO
    ...
    print("Les nombres premiers inférieurs ou égaux à",val_max,"sont :",end='') 
    for i in range(min(len(les_premiers),val_max)):
        if les_premiers[i]==True:
            print(" "+str(i+1)+" ",end='')
    print()        

def main():
    # TODO
    ...
    val_max,prem=int(input("val_max :")),2
    if val_max<2:raise ValueError("val_max doit être supérieur ou égal à 2.")
    L=init_tab(val_max)
    while prem<math.sqrt(val_max):
        filtre(L,prem)
        flag=True
        for i in range(prem,val_max):
            if L[i]==True:
                prem=i+1
                flag=False
                break
        if flag==True:break
    affiche(L,val_max)    

if __name__ == "__main__":
    main()
