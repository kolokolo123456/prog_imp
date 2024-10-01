"""
Un module pour générer des images au format SVG.

Ce module fournit diverses fonctions pour générer des éléments SVG
sous forme de chaînes de caractères.
Ces chaînes DOIVENT être écrites dans un fichier en respectant la
structure SVG pour obtenir une image valide.
"""


# À implémenter dans 'TP2. Module SVG'
def genere_balise_debut_image(largeur, hauteur):
    """
    Retourne la chaîne de caractères correspondant à la balise ouvrante pour
    décrire une image SVG de dimensions largeur x hauteur pixels. Les paramètres
    sont des entiers.

    Remarque : l'origine est en haut à gauche et l'axe des Y est orienté vers le
    bas.
    """
    # TODO
    ...
    k=(float,int)
    if type(largeur) not in k or type(hauteur) not in k or largeur<0 or hauteur<0:raise TypeError("Il s'agit d'un nombre positif svp!")
    return f"<svg width='{largeur}' height='{hauteur}' style=\"background-color:black;\">"    


# À implémenter dans 'TP2. Module SVG'
def genere_balise_fin_image():
    """
    Retourne la chaîne de caractères correspondant à la balise svg fermante.
    Cette balise doit être placée après tous les éléments de description de
    l'image, juste avant la fin du fichier.
    """
    # TODO
    ...
    
    return "</svg>"    


# À implémenter dans 'TP2. Module SVG'
def genere_balise_debut_groupe(epaisseur_ligne,couleur_ligne='none', couleur_remplissage='none'):
    """
    Retourne la chaîne de caractères correspondant à une balise ouvrante
    définissant un groupe d'éléments avec un style particulier. Chaque groupe
    ouvert doit être refermé individuellement et avant la fermeture de l'image.

    Les paramètres de couleur sont des chaînes de caractères et peuvent avoir
    les valeurs :
    -- un nom de couleur reconnu, par exemple "red" ou "black" ;
    -- "none" qui signifie aucun remplissage (attention ici on parle de la chaîne
        de caractère "none" qui est différente de l'objet None).

    Le paramètre d'épaisseur est un nombre positif ou nul, représentant la
    largeur du tracé d'une ligne en pixels.
    """
    # TODO
    ...
    if type(couleur_ligne)!=str or type(couleur_remplissage)!=str:raise TypeError("La couleur doit prendre la forme de chaine de caractère!\nExemple:'red','black'")
    if type(epaisseur_ligne) not in (float,int) or epaisseur_ligne<0:raise TypeError("L'épaisseur est un nombre positif.")
    return f"<g stroke='{couleur_ligne}' stroke-width='{epaisseur_ligne}' fill='{couleur_remplissage}'>"
        

# À implémenter dans 'TP2. Module SVG'
def genere_balise_fin_groupe():
    """
    Retourne la chaîne de caractères correspondant à la balise fermante pour un
    groupe d'éléments.
    """
    # TODO
    ...
    return '</g>'


# À implémenter dans 'TP2. Module SVG'
def genere_cercle(centre, rayon,stroke='none',fill='none'):
    """
    Retourne la chaîne de caractères correspondant à un élément SVG représentant
    un cercle (ou un disque, cela dépend de la couleur de remplissage du groupe
    dans lequel on se trouve).

    centre est une structure de données de type tuple de deux nombres, et rayon
    un nombre de pixels indiquant le rayon du cercle.
    """
    # TODO
    ...
    k=(float,int)
    if type(centre)!=tuple or len(centre)!=2 or type(centre[0]) not in k or type(centre[1]) not in k:raise TypeError('centre est un tuple de 2 nombres.')
    if type(rayon) not in k or rayon<0:raise ValueError("rayon est un nombre positif")
    return f"<circle cx='{centre[0]}' cy='{centre[1]}' r='{rayon}' fill=\"{fill}\" stroke=\"{stroke}\"/>"


# À implémenter dans 'TP3. Tortue Logo'
def genere_segment(dep, arr,color='black',strokewidth=1):
    """
    Retourne la chaîne de caractères correspondant à un élément SVG représentant
    un segment. Ce segment relie les points dep et arr qui sont tous les deux
    des tuples de deux nombres.
    """
    # TODO
    ...
    k=(float,int)
    if type(dep)!=tuple or type(arr)!=tuple or len(dep)!=2 or len(arr)!=2:raise TypeError("Les points de départ et d'arrivée sont des tuples à deux nombres")
    if type(dep[0]) not in k or type(dep[1]) not in k or type(arr[0]) not in k or type(arr[1]) not in k:raise TypeError("les élements de dep et arr sont des nombres")
    return f"<line x1=\"{dep[0]}\" y1=\"{dep[1]}\" x2=\"{arr[0]}\" y2=\"{arr[1]}\" stroke='{color}' stroke-width='{strokewidth}' />"


# À implémenter dans `TP Optionnels Échiquier`
def genere_rectangle(top_left, width, height,color_rem,color_cot="none"):
    """
    Retourne la chaîne de caractères correspondant à un élément SVG représentant un rectangle.
    """
    # TODO
    ...
    return f"<rect x=\"{top_left[0]}\" y=\"{top_left[1]}\" width=\"{width}\" height=\"{height}\" fill=\"{color_rem}\" stroke=\"{color_cot}\"/>"


# À implémenter dans `TP7. Kaléidoscope`
def genere_polygone(points,fill="red",stroke="none"):
    """
    Retourne la chaîne de caractères correspondant à un élément SVG
    représentant un polygone. `points` est un tableau de points qui
    sont eux mêmes des tuples de deux nombres.
    """
    # TODO
    ...
    out="<polygon points=\""
    for i in range(len(points)):
        if i!=len(points)-1:
            out=out+str(points[i][0])+","+str(points[i][1])+" "
        else:
            out=out+str(points[i][0])+","+str(points[i][1])+"\""    
    out=out+" style=\"fill:"+fill+";stroke:"+stroke+";stroke-width:1\" />"
    return out

# À implémenter dans `TP7. Kaléidoscope`
def genere_balise_debut_groupe_transp(niveau_opacite):
    """
    Retourne la chaîne de caractères correspondant à une balise ouvrant un
    groupe d'éléments qui, dans son ensemble, sera partiellement transparent.
    Les éléments qui composent le groupe se masquent les uns les autres dans
    l'ordre d'apparition (ils ne sont pas transparents entre eux).
    `niveau_opacite` doit être un nombre entre 0 et 1. Ce groupe doit être
    refermé de la même manière que les groupes définissant un style.
    """
    # TODO
    ...
    return f"<g fill-opacity=\"{niveau_opacite}\">"


# À implémenter dans `TP8. Plateau`
def genere_zone_colorie(x_min, y_min, largeur, hauteur, couleur_remplissage,couleur_ligne):
    """
    Retourne la chaîne de caractères correspondant à un élément qui colorie une
    zone rectangulaire de la couleur indiquée
    """
    # TODO
    ...
    return genere_rectangle((x_min,y_min), largeur, hauteur, couleur_remplissage, couleur_ligne)



# À implémenter dans `TP8. Plateau`
def genere_texte(x_min, y_bas, contenu, hauteur,couleur="red"):
    """
    Retourne la chaîne de caractères correspondant à un élément SVG représentant
    un texte. Place le texte à la position indiquée. x_min est l'abscisse du
    début du texte. y_bas est l'ordonnée de la ligne de base du texte (le bas
    d'une lettre telle que “n”). Attention, ce n'est pas l'ordonnée maximale
    puisque certaines lettres descendent sous cette ligne (g, j, p, q, y). Le
    paramètre hauteur définit la taille de police (c'est-à-dire la hauteur d'une
    ligne de texte)
    """
    # TODO
    ...
    return f"<text x=\"{x_min}\" y=\"{y_bas}\" front_size=\"{hauteur}\" fill=\"{couleur}\">"+contenu+"</text>"

