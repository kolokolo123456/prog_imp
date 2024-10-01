#!/usr/bin/env python3


"""Jeu du solitaire."""


import subprocess
import sys
import plateau

VIDE = 0
PION = 1

VOISINS = [
    [1, 2, None, None, None, None],
    [3, 4, 2, 0, None, None],
    [4, 5, None, None, 0, 1],
    [6, 7, 4, 1, None, None],
    [7, 8, 5, 2, 1, 3],
    [8, 9, None, None, 2, 4],
    [10, 11, 7, 3, None, None],
    [11, 12, 8, 4, 3, 6],
    [12, 13, 9, 5, 4, 7],
    [13, 14, None, None, 5, 8],
    [None, None, 11, 6, None, None],
    [None, None, 12, 7, 6, 10],
    [None, None, 13, 8, 7, 11],
    [None, None, 14, 9, 8, 12],
    [None, None, None, None, 9, 13],
]

def calcule_solution(plat,out=[]):
    """Renvoie la suite des coups à jouer **à l'envers** pour gagner.

    Renvoie la suite des coups à jouer sous la forme d'une list, ordonnée
    à l'envers. Par exemple, après exécution de la ligne :

    coups = calcule_solution(plat)

    on aura coups[0] qui contient le **dernier** coup à jouer pour gagner,
    coups[1] l'avant-dernier, ..., et coups[-1] le **premier** coup à jouer
    à partir de l'état actuel du plateau plat.

    Renvoie None si le plateau n'est pas gagnant et on a essayé (en vain)
      tous les coups possibles.
    """
    cases=plat.cases
    i=0
    for case in cases:
        if case==PION:i+=1
    if i==1:
        return out
    for case in range(14):
        if cases[case]==VIDE:
            for voisin in range(6):
                if VOISINS[case][voisin]!=None and cases[VOISINS[case][voisin]]==PION and VOISINS[VOISINS[case][voisin]][voisin]!=None and cases[VOISINS[VOISINS[case][voisin]][voisin]]:
                    plat1=plat
                    plat1.cases[case]=PION
                    plat1.cases[VOISINS[case][voisin]]=VIDE
                    plat1.cases[VOISINS[VOISINS[case][voisin]][voisin]]=VIDE
                    sol=calcule_solution(plat1,[case,VOISINS[VOISINS[case][voisin]][voisin]]+out)
                    if sol!=None:
                        return sol
    else:
        return None                




def demande_coup(plat):
    """Demande quel coup jouer à l'utilisateur."""
    try:

        # Demande la case à jouer
        print("tapez ^C pour arrêter et lancer la résolution")
        depart = int(input("ou alors \n  donnez une case de départ: "))
        if plat.cases[depart] == plateau.VIDE:
            print("  case de départ invalide")
            raise ValueError

        # Demande la case d'arrivée
        arrivee = int(input("  donnez une case d'arrivée: "))
        if plat.cases[arrivee] == plateau.PION:
            print("  case d'arrivée invalide")
            raise ValueError

        # On vérifie que le mouvement est valide, c'est à dire
        # qu'il y a un pion entre le départ et l'arrivée.
        # Le FAMEUX "for else" de Python : c'est QUOi CE TRUC ??
        for direction, milieu in enumerate(plateau.VOISINS[depart]):
            if milieu is not None:
                apres_milieu = plateau.VOISINS[milieu][direction]
                if apres_milieu is not None and apres_milieu == arrivee:
                    break
        else:
            print("  mouvement invalide")
            raise ValueError
        # Nous (mais pas pylint) savons qu'ici milieu est défini
        # pylint: disable=undefined-loop-variable
        if plat.cases[milieu] == plateau.VIDE:
            print("  mouvement invalide")
            raise ValueError
        return depart, milieu, arrivee

    # Ici on fait suivre l'exception
    except KeyboardInterrupt:
        raise

    # Ici on redemande à l'utilisateur car il
    # a joué un coup invalide.
    # pylint, laisse nous tranquille, on gère !
    except:  # pylint: disable=bare-except
        return demande_coup(plat)


def main():
    """Lance une partie de solitaire."""

    # On determine si on est dans terminology ou non
    # pour savoir comment afficher le plateau :
    # SVG ou textuel ?
    try:
        subprocess.check_call(["tycat"])
        in_terminology = True
    except subprocess.CalledProcessError:  # Si le programme n'a pas renvoyé zéro
        in_terminology = False
    except FileNotFoundError:  # Si le programme n'est pas trouvé dans le PATH
        in_terminology = False

    # On joue tant que ^C n'est pas tapé ou qu'on a pas gagné
    plat = plateau.Plateau()
    while not plateau.est_gagnant(plat):
        plateau.affiche(plat, in_terminology)
        try:
            coup = demande_coup(plat)
        except KeyboardInterrupt:  # sur ^C
            break
        print(f"on joue de {coup[0]} a {coup[2]}")
        plateau.joue_coup(plat, coup)

    # Si le joueur humain a gagné, on s'arrête
    if plateau.est_gagnant(plat):
        print("Gagné !!!")
        sys.exit(0)

    # Sinon on demande la solution pour finir à notre
    # intelligence artificielle (fallait le placer ce
    # terme dans le cours BPI quand même !)
    suite = calcule_solution(plat)
    print()
    if suite:
        print("suite de coups possible pour terminer :")
        for debut, _, arrivee in reversed(suite):
            print("(", debut, ", ", arrivee, ")", sep="", end=" ")
        sys.exit(0)
    else:
        print("pas moyen d'aller plus loin !!!")
        sys.exit(1)


if __name__ == "__main__":
    main()
