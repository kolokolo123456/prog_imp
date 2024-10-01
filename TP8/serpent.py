#!/usr/bin/env python3

import svg

largeur,hauteur=1800,1600
taille_case=(40,40)
nb_cases=(largeur//taille_case[0],hauteur//taille_case[1])
liste_points=[[(taille_case[0]*i,taille_case[1]*j) for i in range(nb_cases[0])] for j in range(nb_cases[1]) if j%2==0 or (j==nb_cases[1]-1 and (j-1)%4==0) or (j==0 and (j-3)%4==0)][::-1]

def main():
    print(svg.genere_balise_debut_image(largeur,hauteur))
    print(svg.genere_rectangle((0,0),largeur,hauteur,"gray","black"))
    c=1
    for j in range(nb_cases[1]-1,-1,-1):
        if j%4==0:
            for i in range(nb_cases[0]-1,-1,-1):          
                print(svg.genere_rectangle((taille_case[0]*i,taille_case[1]*j),taille_case[0],taille_case[1],"none","black"))
                print(svg.genere_texte(taille_case[0]*(i+0.25),taille_case[1]*(j+0.5), str(c),taille_case[1]))
                c+=1
            print(svg.genere_rectangle((0,taille_case[1]*(j-1)),taille_case[0],taille_case[1],"none","black"))
            print(svg.genere_texte(taille_case[0]/4,taille_case[1]*(j-0.5), str(c),taille_case[1]))
            c+=1  
        elif (j-2)%4==0:
            for i in range(nb_cases[0]):          
                print(svg.genere_rectangle((taille_case[0]*i,taille_case[1]*j),taille_case[0],taille_case[1],"none","black"))
                print(svg.genere_texte(taille_case[0]*(i+0.25),taille_case[1]*(j+0.5), str(c),taille_case[1]))
                c+=1
            print(svg.genere_rectangle((taille_case[0]*(nb_cases[0]-1),taille_case[1]*(j-1)),taille_case[0],taille_case[1],"none","black"))
            print(svg.genere_texte(taille_case[0]*(nb_cases[0]-0.75),taille_case[1]*(j-0.5), str(c),taille_case[1]))
            c+=1                      
    print(svg.genere_balise_fin_image()) 

main()       


