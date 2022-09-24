import os
from PIL import Image


def f1(r,g,b):
    return (g, b, r)

def rose(r,g,b):
    return (r+g)//2,(g+b)//2,(b+r)//2

def cyan(r,g,b):
    return (b,g,r)

def blanc (r,g,b):
    return (r,r,r)

def vert (r,g,b):
    return (abs(r-g)//2,abs(g-b)*2,abs(b-r))

def rouge (r,g,b): #(pour toi Arthur)
    return (r,0,0)

def change_color(name_piece,f_transf):
    
    """_ Cette fonction prend en argument le nom d'une pièce et une fonction réalisant une combinaison linéraire des composantes rgb de l'image de la pièce (initialement jaune)
    Elle crée ensuite une image avec la nouvelle couleur dans un nouveau dossier_
    """

    img = Image.open(f'Djambi//images//pieces//yellow//{name_piece}.png')
    rgb_img = img.convert('RGB')
    (larg,long) = img.size
    for x in range(larg):
        for y in range(long):
            r,g,b = rgb_img.getpixel((x,y))
            if (r,g,b) != (0,0,0):
                r,g,b = f_transf(r,g,b)
                img.putpixel((x,y),(r,g,b))
    #img.show()
    img.save(f'Djambi//iamges//pieces//{f_transf.__name__}//{name_piece}.png')
    
