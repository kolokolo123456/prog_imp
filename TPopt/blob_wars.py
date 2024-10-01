#!/usr/bin/env python3

import random

BLUE="B"
RED="R"

def int_to_str(nb):
    out=str(nb)
    if len(out)==1:return "0"+out
    return out

def plateau(cases_bleues,cases_rouges):
    plateau,i=[],63
    for j in range(7,-1,-1):
        l=[]
        for k in range(8):
            if i in cases_bleues:
                l=[[i,BLUE]]+l
            elif i in cases_rouges:
                l=[[i,RED]]+l
            else:        
                l=[[i,None]]+l
            i-=1
        plateau.append(l)
    return plateau

def droite(num_case):
    return num_case not in [8*i-1 for i in range(1,9)]

def gauche(num_case):
    return num_case not in [8*i for i in range(8)]

def haut(num_case):
    return num_case not in [i for i in range(56,64)]

def bas(num_case):
    return num_case not in [i for i in range(8)]

def verifier_case(num_case,direction):
    if direction=='g' and gauche(num_case):
        return num_case-1
    elif direction=='d' and droite(num_case):
        return num_case+1
    elif direction=='h' and haut(num_case):
        return num_case+8
    elif direction=='b' and bas(num_case):
        return num_case-8
    elif direction=='hd' and haut(num_case) and droite(num_case):
        return num_case+9
    elif direction=='hg' and haut(num_case) and gauche(num_case):
        return num_case+7
    elif direction=='bd' and bas(num_case) and droite(num_case):
        return num_case-7
    elif direction=='bg' and bas(num_case) and gauche(num_case):
        return num_case-9

def selectionner_case(couleur,cases_bleues,cases_rouges):
    for i in range(3):
        num_case=int(input("Numéro de case: "))
        if (couleur=='B' and num_case in cases_bleues) or (couleur=='R' and num_case in cases_rouges):
            saut=int(input("Saut? "))
            direction=input('Direction: ')
            case_valide=False
            if saut==0:
                case_valide=verifier_case(num_case,direction)
            elif saut==1:
                direction2=input('2ème direction: ')
                case_valide=verifier_case(verifier_case(num_case,direction),direction2)    
            if case_valide!=None:
                if couleur=='B' and case_valide not in cases_bleues:
                    cases_bleues.append(case_valide)
                    if saut==1:cases_bleues.remove(num_case)
                elif couleur=='R' and case_valide not in cases_rouges:
                    cases_rouges.append(case_valide)
                    if saut==1:cases_rouges.remove(num_case)
                break
        print("Case non valide.")

def afficher_plateau(plateau):
    for ligne in plateau:
        k=""
        for i in ligne:
            if i[1]==RED:k+="\U0001F534 "
            elif i[1]==BLUE:k+="\U0001F535 "
            else:
                k+=int_to_str(i[0])+" "
        print(k)

def partie():
    cases_bleues,cases_rouges=[56,63],[0,7]
    afficher_plateau(plateau(cases_bleues,cases_rouges))
    couleurs=['R','B']
    n=random.randint(0,1)
    while len(cases_rouges)+len(cases_bleues)<64:
        couleur=couleurs[n]
        if n==0:print("Couleur rouge")
        if n==1:print("Couleur bleue")
        selectionner_case(couleur,cases_bleues,cases_rouges)
        afficher_plateau(plateau(cases_bleues,cases_rouges))
        n=(n+1)%2
    if len(cases_rouges)<len(cases_bleues):print("Le joueur bleu a gagné!") 
    elif len(cases_rouges)>len(cases_bleues):print("Le joueur rouge a gagné!") 
    else:
        print("Égalité!")  

partie()      




