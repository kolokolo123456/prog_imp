#!/usr/bin/env python3

def pivote1(tableau, indice_pivot):
    if tableau==[]:return tableau
    inf,sup,pivot=[],[],tableau[indice_pivot]
    for i in range(len(tableau)):
        if i==indice_pivot:continue
        if tableau[i]<=pivot:inf.append(tableau[i])
        else:
            sup.append(tableau[i])
    return inf,sup

def pivote2(tableau,indice_pivot):
    if len(tableau)<2:return tableau
    val=tableau[indice_pivot]
    for i in range(len(tableau)):
        if tableau[i]>val and i<indice_pivot:
            for j in range(i,indice_pivot):
                tableau[j],tableau[j+1]=tableau[j+1],tableau[j]
            indice_pivot-=1
        elif tableau[i]<=val and i>indice_pivot:
            for j in range(i-1,indice_pivot-1,-1): 
                tableau[j],tableau[j+1]=tableau[j+1],tableau[j]
            indice_pivot+=1       
    return tableau            




        
print(pivote2([3,0,10,1,6,9,5,3,9,0,5,8,9,8,4,2,0,9,6,2],0))