#!/usr/bin/env python3

import random
import svg
import math

hauteur,largeur=1000,1000 #dimensions de l'image
prbr=[(largeur//2,9*hauteur//10),(largeur//2,3*hauteur//5)] #premiere branche
nb_s_branches=3 #nombre de sous branches pour chaque branche
coef_reduction=0.6

def distance(x1,x2):
    """
    distance euclidienne
    """
    return math.sqrt(((x1[0]-x2[0])**2)+((x1[1]-x2[1])**2))

def comb_lineaire(x1,x2,a,b):
    """
    retourne le point a*x1+b*x2
    """  
    return (a*x1[0]+b*x2[0],a*x1[1]+b*x2[1])  

def dessine_branche(x1,x2,epaisseur):
    """
    dessine branche verticale du point x1 vers x2
    """
    print(svg.genere_segment(x1,x2,epaisseur))

def selectionne_point(branche):
    """
    selectionne un point aléatoire appartenant à une branche
    ce point sera le début d'une nouvelle sous branche
    ici, branche est une liste de 2 points 
    """
    t=random.random()
    return (t*branche[0][0]+(1-t)*branche[1][0],t*branche[0][1]+(1-t)*branche[1][1])

def selectionne_s_branche_aleatoire(branche,alpha):
    """
    retourne une sous branche aléatoire d'une branche
    cette sous branche est plus courte que sa mère
    """
    d=distance(branche[0],branche[1])
    x1=selectionne_point([comb_lineaire(branche[0],branche[1],1/2,1/2),branche[1]])
    alpha+=random.random()*math.pi/2-math.pi/4
    x2=(x1[0]+d*coef_reduction*math.sin(alpha),x1[1]-d*coef_reduction*math.cos(alpha))
    return [x1,x2],alpha

def dessine_arbre(branche,eps,alpha,epaisseur): 
    d=distance(branche[0],branche[1])
    if d>eps:
        dessine_branche(branche[0],branche[1],epaisseur)
        for _ in range(nb_s_branches):
            branche1,alpha1=selectionne_s_branche_aleatoire(branche,alpha)
            dessine_arbre(branche1,eps,alpha1,epaisseur*coef_reduction)  
    else:
        print(svg.genere_cercle(branche[1],1,'green','green'))    #epaisseur de feuille=2     


def main():
    print(svg.genere_balise_debut_image(1000,1000))
    print(svg.genere_balise_debut_groupe(1,"#8B4513"))
    dessine_arbre(prbr,2,0,10)
    print(svg.genere_balise_fin_groupe())
    print(svg.genere_balise_fin_image())

main()    

