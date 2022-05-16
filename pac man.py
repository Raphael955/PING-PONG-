# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def afficher(laby , pac_man, liste_fantome):
    print (chr(0x1F47B))

pac_man = {"pos_x" : 0, 
          "pos_y" : 0,
          "vies"  : 3,
          "style" : "normal",
          "vitesse" : 5,
          "direction" : "droite",}
          
# Création des fantômes 
liste_fantome = []
fantome1= {"pos_x" : 0,
          "pos_y" : 0,
          "vitesse" : 4.5,
          "direction" : "droite",
          "vies" : 1}
fantome2= {"pos_x": 0,
          "pos_y": 0,    
          "vitesse": 4.5,
          "direction" : "droite",
          "vies" : 1}
fantome3= {"pos_x" : 0,
          "pos_y" : 0,
          "vitesse": 4.5,
          "direction" : "droite",
          "vies" : 1}

# Création du labyrinthe 
laby = Terrain = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 2, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0,
    0, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]
"""
0 = mur
1 = Pac Gommme
2 = Cerise 

"""



    
print(pac_man["pos_x"])
print(pac_man["pos_y"])

for ligne in laby:
    x=0
    for case in ligne :
        if case == 0:
            caractere = chr(0x1F535)
        elif case == 1:
            ""
        elif case == 2:
            caractere = chr(0x1F36C)
        if pac_man ("pos_x")==x and pac_man ("pos_y")==y:
            caractere = chr(0x1F34B)
            
...
print(caractere,end="")
x+1=




          
