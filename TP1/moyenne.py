#!/usr/bin/env python3

"""Illustration de pylint"""


def affiche_moyenne(note_projet, note_exam):
    """cette fonction calcule la moyenne d'un élève"""
    print((1 * note_projet + 3 * note_exam) / 4)


affiche_moyenne(12,14)
