#########################################
# groupe  2 MPCI 6
# Claude CHIBOUT
# Cyril CLOVIS
# Dylan THUILLIER
# Abdel karim BOURAOUI
# Ahmadou bamba SOUM
# Olivier GABRIEL
# https://github.com/uvsq22005256/projet_incendie
# https://discord.gg/fNQpuPM3yQ
#########################################
#Import des fonctions
import tkinter as tk

#########################################
#Variable
largeur = 500
hauteur = 500
couleur_canv= 'grey30'
couleur_quadr = 'grey60'
cote = 20
root = tk.Tk()
canvas = tk.Canvas(root, bg=couleur_canv, width = largeur, height=hauteur)


#########################################
#Fonction
def quadrillage() :
 """Dessine un quadrillage formé de carrés de côté Cote"""
y = 0
while y <= hauteur :
    canvas.create_line((0,y), (largeur,y), fill=couleur_quadr)
    y += cote
x = 0    
while x <= largeur :
    canvas.create_line((x,0), (x, hauteur), fill=couleur_quadr)
    x += cote


#########################################
#Programme principal
root.title('Projet Incendie')
quadrillage()





#########################################
#Création des widgets
canvas.grid()
root.mainloop()