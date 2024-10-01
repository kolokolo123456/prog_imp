#!/usr/bin/env python3

import svg

NBR_CASES=(8,8)
TAILLE_CASE = 75
COULEURS = ("white", "black")

def dessine_ligne(prem_coul, abs,ord):
    print(svg.genere_rectangle((TAILLE_CASE*abs+5,TAILLE_CASE*ord+5),TAILLE_CASE,TAILLE_CASE,prem_coul))

def main():
    k=0
    print(svg.genere_balise_debut_image(610,610))
    print(svg.genere_rectangle((0,0),610,610,"red"))
    for i in range(NBR_CASES[0]):
        k=(k+1)%len(COULEURS)
        for j in range(NBR_CASES[1]):
            dessine_ligne(COULEURS[k],i,j)
            k=(k+1)%len(COULEURS)
    print(svg.genere_balise_fin_image())  
main()        
