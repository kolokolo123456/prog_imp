#!/usr/bin/env python3

def main():
    prix=42
    i=0
    while i!=prix:
        i=int(input("deviner prix: "))
        if i<0:
            print("Comment ? Vous me pensez assez tordu pour avoir choisi un prix négatif ???")
            continue
        if i<prix:print("Vous avez donné un nombre inférieur au prix, réssayer.")
        elif i>prix:print("Vous avez donné un nombre supérieur au prix, réssayer.")
    print("Bien, le vrai prix est",prix)
main()    
    