#!/usr/bin/env python3

"""Illustration simple des f-strings."""


def teste_fstrings():
    """Utilisation de f-strings pour afficher un message."""
    prenom = "Alexia"
    age = 8
    message_a_afficher = f"{prenom} a {age} ans"
    print(message_a_afficher)


teste_fstrings()

def convertit_point_en_chaine(x, y):
    return f"({x},{y})"

print(convertit_point_en_chaine(12.2,3.3))
