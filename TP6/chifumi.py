import random as rd
rd.seed(40)
j=["pierre","feuille","ciseaux"]
x=int(input("Tu veux jouer Chifumi? Si oui clique sur 1,sinon tape sur 0:\n"))
while x not in (0,1):x=int(input("Tu veux jouer Chifumi? Si oui clique sur 1,sinon tape sur 0:\n"))
while x==1:
    a=int(input("Choisis entre pierre(tape sur 0),feuille(1) et ciseaux(2):\n"))
    while a not in (0,1,2):a=int(input("Choisis entre pierre(tape sur 0),feuille(1) et ciseaux(2):\n"))
    b=rd.randint(0,2)
    print("Ton choix: ",j[a],"\nMon choix: ",j[b])
    if a==b:print("Égalité.")
    elif (a<b and (a,b)!=(0,2)) or (a,b)==(2,0):print("J'ai gagné!")
    elif b<a or (a,b)==(0,2):
        print("Tu as gagné!")
    x=int(input("Rejouer ? Oui(1) , Non(0)\n")) 
    while x not in (0,1):x=int(input("Rejouer ? Oui(1) , Non(0)\n"))   