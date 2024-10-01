#! /usr/bin/env python3

from random import randint,random

def random_circle(largeur,hauteur):
    return randint(1,largeur),randint(1,hauteur),random()*min(largeur,hauteur)/2

def pt_dans_cercle(pt,centre,rayon):
    return (pt[0]-centre[0])**2+(pt[1]-centre[1])**2<=rayon**2

l=input("Largeur: ")
h=input("Hauteur: ")
print("P2\n"+l+" "+h+"\n255")
l,h=int(l),int(h)
(x1,y1,r1)=random_circle(l,h)
(x2,y2,r2)=random_circle(l,h)
for y in range(1,h+1):
    ligne=""
    for x in range(1,l+1):
        if pt_dans_cercle((x,y),(x1,y1),r1) or pt_dans_cercle((x,y),(x2,y2),r2):
            ligne+=str(randint(0,255))
        else:
            ligne+="255"
        if x!=l:
            ligne+=" "  
    print(ligne)          
                
