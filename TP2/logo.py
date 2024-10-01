"""Module tortue logo.

Ce module implémente les primitives graphiques basiques
d'une tortue logo.
"""

import svg
import math


def avance(abscisse, ordonnee, direction, crayon_en_bas, distance):
    """Fait avancer la tortue.

    Fait avancer la tortue dans la direction donnée et de la distance donnée.
    Affiche le segment SVG correspondant sur la sortie standard
    si le crayon est en bas.

    Renvoie la nouvelle position de la tortue sous la forme
    d'un tuple à deux entiers.
    """
    # TODO
    ...
    if distance>0:
        arr=(abscisse-distance*math.cos(math.radians(direction)),ordonnee-distance*math.sin(math.radians(direction)))
        if crayon_en_bas==True:print(svg.genere_segment((abscisse,ordonnee),arr)) 
    return arr             


def tourne_droite(direction, angle):
    """
    Fait tourner la tortue à droite.

    Fait tourner la tortue à partir de direction en tournant
    à droite de l'angle donné (en degrés).

    Renvoie la nouvelle direction.
    """
    # TODO
    ...
    return direction+angle


def tourne_gauche(direction, angle):
    """
    Fait tourner la tortue à droite.

    Fait tourner la tortue à partir de direction en tournant
    à droite de l'angle donné (en degrés).

    Renvoie la nouvelle direction.
    """
    # TODO
    ...
    return direction-angle

