#!/usr/bin/env python3

""" LABYRINTHE"""

import svg
import random

hauteur,largeur=2000,2000
porte=5
eps=4 
remp='white'
RGB=['red','green','blue']

def dessine_mur(x1,x2,couleur):
    print(svg.genere_segment(x1,x2,couleur))

def mur_plus_proche(mur,flg1,flg2,lx,ly):
    """
    flg1 indique si le mur est vertical ou horizental, elle prend en valeur soit 'v' ou 'h'
    flg2 indique si on cherche le plus proche à droite ou bas (flg2=0), gauche ou haut (flg2=1)
    """
    if flg1=='v':
        xm=mur[0][0]
        if flg2==0:
            return min([lx[i] for i in range(len(lx)) if lx[i]>xm])
        elif flg2==1:
            return max([lx[i] for i in range(len(lx)) if lx[i]<xm])
    elif flg1=='h':
        ym=mur[0][1]
        if flg2==0:
            return min([ly[i] for i in range(len(ly)) if ly[i]>ym])
        elif flg2==1:
            return max([ly[i] for i in range(len(ly)) if ly[i]<ym])    


def dessine_murs(mur,flg,lx,ly): 
    """
    flg indique si le mur est vertical ou horizental, elle prend en valeur soit 'v' ou 'h'
    """
    if flg=='v':
        hauteur_mur=abs(mur[1][1]-mur[0][1])
        if hauteur_mur<=eps*porte:
            return
        dessine_mur(mur[0],mur[1],random.choice(RGB))
        prt=random.random()*(hauteur_mur-porte)
        print(svg.genere_segment((mur[0][0],mur[0][1]+prt),(mur[0][0],mur[0][1]+prt+porte),remp))
        ymur1=random.random()*hauteur_mur/2
        ymur2=random.random()*hauteur_mur/2
        while 0<ymur1+hauteur_mur/4-prt<porte or 0<ymur2+hauteur_mur/4-prt<porte:
            ymur1=random.random()*hauteur_mur/2
            ymur2=random.random()*hauteur_mur/2
        mur1=((mur[0][0],mur[0][1]+hauteur_mur/4+ymur1),(mur_plus_proche(mur,flg,0,lx,ly),mur[0][1]+hauteur_mur/4+ymur1))
        mur2=((mur_plus_proche(mur,flg,1,lx,ly),mur[0][1]+hauteur_mur/4+ymur2),(mur[0][0],mur[0][1]+hauteur_mur/4+ymur2))
        dessine_murs(mur1,'h',lx+[mur[0][0]],ly)
        dessine_murs(mur2,'h',lx+[mur[0][0]],ly)
    elif flg=='h':
        largeur_mur=abs(mur[1][0]-mur[0][0])
        if largeur_mur<eps*porte:
            return
        dessine_mur(mur[0],mur[1],random.choice(RGB))
        prt=random.random()*(largeur_mur-porte)
        print(svg.genere_segment((mur[0][0]+prt,mur[0][1]),(mur[0][0]+prt+porte,mur[1][1]),remp))
        xmur1=random.random()*largeur_mur/2
        xmur2=random.random()*largeur_mur/2
        while 0<xmur1+largeur_mur/4-prt<porte or 0<xmur2+largeur_mur/4-prt<porte:
            xmur1=random.random()*largeur_mur/2
            xmur2=random.random()*largeur_mur/2
        mur1=((mur[0][0]+largeur_mur/4+xmur1,mur[0][1]),(mur[0][0]+largeur_mur/4+xmur1,mur_plus_proche(mur,flg,0,lx,ly)))
        mur2=((mur[0][0]+largeur_mur/4+xmur2,mur_plus_proche(mur,flg,1,lx,ly)),(mur[0][0]+largeur_mur/4+xmur2,mur[0][1]))
        dessine_murs(mur1,'v',lx,ly+[mur[0][1]])
        dessine_murs(mur2,'v',lx,ly+[mur[0][1]])


def main():
    print(svg.genere_balise_debut_image(largeur+2*porte,hauteur+2*porte))
    print(svg.genere_rectangle((porte,porte),largeur, hauteur,remp,color_cot="black"))
    print(svg.genere_segment((porte,porte),(2*porte,porte),remp))
    print(svg.genere_segment((porte+largeur,porte+hauteur),(largeur,porte+hauteur),remp))
    print(svg.genere_balise_debut_groupe(1)) 
    x0=random.random()*largeur/2
    prem_mur=((largeur/4+x0+porte,porte),(largeur/4+x0+porte,hauteur+porte))
    dessine_murs(prem_mur,'v',[porte,porte+largeur],[porte,porte+hauteur]) 
    print(svg.genere_balise_fin_groupe())
    print(svg.genere_balise_fin_image())
      
main()      