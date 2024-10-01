#!/usr/bin/env python3

import sys

STATIONNAIRE=0
CROISSANTE=1
DECROISSANTE=-1

def traite_nombre(suite, type_suite, nombre):
    """Traite le nombre donné vis à vis de la suite donnée.

    Renvoie (True, nouveau_type_suite) si suite est toujours
    une suite monotone après ajout de nombre.
    Renvoie (False, nouveau_type_suite) si la suite a changé
    de sens.
    """
    if suite==[]:return True,0
    diff,nouveau_type_suite=nombre-suite[-1],0
    if diff>0:nouveau_type_suite=1
    elif diff<0:nouveau_type_suite=-1
    if nouveau_type_suite!=0:
        if type_suite==0:return True,nouveau_type_suite
        if nouveau_type_suite==type_suite:return True,type_suite
        else:
            return False,nouveau_type_suite
    return True,type_suite    
    

def main():
    file=open(sys.argv[1],'r')

    plus_longue_suite=[]
    suite=[]
    type_suite=0

    while True:
        line=file.readline()
        if line=='':break
        lst=line.split(" ")
        for i in lst:
            nb=int(i)
            tr=traite_nombre(suite,type_suite,nb)
            if tr[0]:
                suite.append(nb)
                type_suite=tr[1]
            else:
                if len(suite)>len(plus_longue_suite):plus_longue_suite=suite
                suite,type_suite=[suite[-1],nb],tr[1]
    print(plus_longue_suite)                

    file.close()   

main()     