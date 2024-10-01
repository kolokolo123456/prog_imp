#!/usr/bin/env python3

import random
import svg

def couleur_aleatoire():
    r,g,b=random.randint(0,255),random.randint(0,255),random.randint(0,255)
    return f"rgb({r},{g},{b})"

def affiche_triangle(triangle,couleur):
    print(svg.genere_polygone(triangle,couleur))
