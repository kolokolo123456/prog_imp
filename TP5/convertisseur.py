#! /usr/bin/env python3

import svg

print(svg.genere_balise_debut_image(640,480))
print(svg.genere_balise_debut_groupe(2,'red', 'black'))

"""while True:"""
for _ in range(1000):
    x=input()
    y=input()
    """if x:"""
    x,y=int(x),int(y)
    centre=(x,y)
    print(svg.genere_cercle(centre,2))
"""    else:
        break
"""
print(svg.genere_balise_fin_groupe())
print(svg.genere_balise_fin_image()) 
