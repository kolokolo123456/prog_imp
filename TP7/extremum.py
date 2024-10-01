#!/usr/bin/env python3

def extremum(prec, cour, suiv):
    return (cour<prec and cour<suiv) or (cour>prec and cour>suiv)

def main():
    L=[]
    NBE=0
    while True:
        x=int(input("Donner un entier positif:")) 
        if x<0:
            if len(L)>1:
                print(L[-1],"est un extremum.")
                NBE+=1
            print("Nombre total d'extremums:",NBE)
            break
        if L==[]:
            L.append(x)
            print(x,"est un extremum.")
            NBE+=1
        elif len(L)==1 and x!=L[0]:L.append(x)
        elif len(L)>1 and x!=L[-1]:
            L.append(x)
            if extremum(L[-3],L[-2],L[-1]):
                print(L[-2],"est un extremum") 
                NBE+=1   

main()                    
