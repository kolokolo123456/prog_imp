#!/usr/bin/env python3

import sys

allume='\u2588'
alph='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def affichage_prem_colone(N):
    l1=5*' '
    for i in range(1,N+1):
        l1+=str(i)+4*' '
    print(l1)
    print('  +--'+5*(N-1)*'-'+'---+') 

def affichage_colone(colone,lettre):
    l1,l2,l3='  |',lettre+' |','  |'
    for i in colone:
        if i=='\\':break
        if i=='_':
            l1+=5*' '
            l2+=5*' '
            l3+=5*' '
        if i=='.':
            l1+=5*allume
            l2+=5*allume
            l3+=5*allume
    print(l1+'|\n'+l2+'|\n'+l3+'|')       

def affichage_dern_colone(N):
    print('  +--'+5*(N-1)*'-'+'---+')

def affichage(niv,N,H):
    affichage_prem_colone(N)
    for i in range(H):
        affichage_colone(niv[i],alph[i])
    affichage_dern_colone(N) 

def change_etat_case(niv,i,j):
    k=''
    for ch in range(len(niv[0])):
        if ch==j:
            if niv[i][j]=='_':k+='.'
            elif niv[i][j]=='.':k+='_'   
        else:
            k+=niv[i][ch]   
    niv[i]=k              
    if i==len(niv)-1 and j==len(niv[0])-1:niv[i]+='\n'   

def voisins_case(N,H,i,j):
    voisins=[(i,j)]
    if i!=0:voisins.append((i-1,j))
    if j!=0:voisins.append((i,j-1))
    if i!=N-1:voisins.append((i+1,j))
    if j!=H-1:voisins.append((i,j+1))
    return voisins

def change_etat(niv,N,H):
    case=input()
    while not (len(case)==2 and case[0] in alph[:H] and case[1] in [str(i) for i in range(1,N+1)]):case=input()
    i,j=alph.index(case[0]),int(case[1])-1
    for voisin in voisins_case(H,N+1,i,j):change_etat_case(niv,voisin[0],voisin[1])

def tout_eteint(niv):
    et=0
    for i in range(len(niv)):
        for j in range(len(niv[0])):
            if niv[i][j]=='.':return False
    return True            

def main():
    niv=open(sys.argv[1],'r').readlines()
    N,H,i=len(niv[0])-1,len(niv),0
    affichage(niv,N,H)
    while not tout_eteint(niv):
        change_etat(niv,N,H)
        affichage(niv,N,H)
        i+=1
    print("Félicitations, vous avez terminé ce niveau en",i,"étapes.") 

main()       
