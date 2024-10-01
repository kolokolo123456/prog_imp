#!/usr/bin/env python3

import matplotlib.pyplot as plt
import time
import random

def tri_insertion(tab):
    if len(tab)>1:
        for i in range(1,len(tab)):
            while tab[i]<tab[i-1] and i>0:
                tab[i],tab[i-1]=tab[i-1],tab[i]
                i-=1

def tri_selection(tab):
    if len(tab)>1:
        for i in range(1,len(tab)):
            id_min=i-1
            for j in range(i,len(tab)):
                if tab[j]<tab[id_min]:
                    id_min=j
            tab[i-1],tab[id_min]=tab[id_min],tab[i-1]

def tri_sort(tab):
    tab.sort()            

def mesure_temps(fonction,tab):
    deb=time.time()
    fonction(tab)
    fin=time.time()
    return fin-deb

def main():
    X=[i for i in range(500)]
    Y_insert=[mesure_temps(tri_insertion,[random.randint(1,50) for j in range(i)]) for i in range(500)]                                   
    Y_select=[mesure_temps(tri_selection,[random.randint(1,50) for j in range(i)]) for i in range(500)]                                   
    Y_sort=[mesure_temps(tri_sort,[random.randint(1,50) for j in range(i)]) for i in range(500)] 
    plt.plot(X,Y_insert,color='r',label="tri insertion")
    plt.plot(X,Y_select,color='b',label='tri selection')                                  
    plt.plot(X,Y_sort,color='g',label='fonction sort') 
    plt.legend()
    plt.title("Comparaison entre les algorithmes de tri en terme de temps")
    plt.xlabel("Longueur du tableau")
    plt.ylabel("temps en secondes")
    plt.show()   

main()                                  