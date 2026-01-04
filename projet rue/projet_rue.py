from turtle import*
from random import*
speed(0)

def couleur_aleatoire():
    """
La fonction couleur_aleatoire() permet de pouvoir mettre de couleur de facon aléatoire
"""
    colormode(255)
    r,g,b = randint(0,255),randint(0,255),randint(0,255)#couleurs aleatoires
    return (r,g,b)

def sol():
    """
la fonction sol() trace un trait pour définir le niveau de la rue
"""
    pensize(5)
    up()
    goto(-400,-200)
    down()
    #dessine la rue
    forward(800)
    pensize(1)

def rectangle(x,y,w,h,couleur):
    """
La fonction rectangle(x,y,w,h,couleur) permet de tracer un rectangle avec une couleur
Elle à pour paramètre les coordonnées (x,y) qui correspondent au milieu de la base du rectangle,
la largeur est représenter par w, la hauteur par h et la couleur.
"""
    up()
    goto(x,y)#aller base du rectangle
    down()
    
    begin_fill()
    fillcolor(couleur)
    
    for i in range(2):
        forward(w/2)
        left(90)
        forward(h)
        left(90)
        forward(w/2)#tracer le rectangle en fonction de hauteur h et de largeur w
    
    end_fill()

def route_herbes():
    """
la fonction route() permet de faire un fond qui correspond à une route
"""
    rectangle(0,-200,-800,-50,"grey") #permet de faire le fond qui correspond à la route
    pensize(3)
    x=-350 #correspond à l'abscisse ou sera fait le 1er rectangle qui sur la route
    for i in range (15):
            rectangle(x,-225,30,10,"white")
            x+=50#répétition 15 fois de rectangles qui représente la lignes de rives sur la route avec un séparation entre chaque milieu de rectangle de 50 pixels  chaque rectangle fera 30 pixels de longueur et 10 de hauteur 
    up()
    goto(-400,-250)
    down()
    
    forward(800)
    pensize(1)
    rectangle(0,-600,-800,350,"green") #permet de faire le fond qui correspond à l'herbe
    
def lune():
    """
La fonction lune permet de tracer une lune 
"""
    up()
    goto(250,300)#permets d'aller au coordonnées de ou on va commencé la lune
    down()
    begin_fill()
    fillcolor("yellow")#permet que la lune sois jaune
    left(180)
    circle(50,250)#fait presque les 3/4 d'un cercle
    left(290)#se dirige pour pouvoir faire un autre cercle qui va se relié à l'autre de départ
    circle(50,-110)#fait un cercle qui se relis au début de l'autre de façon à que sa représente une lune
    end_fill()
    left(110) #redéfini l'angle à 0
    
def soleil():
    """
La fonction soleil permet de faire un soleil 
"""
    up()
    goto(250,300)#permets d'aller au coordonnées de ou on va commencé le soleil
    down()
    begin_fill()
    fillcolor("yellow")#permet que le soleil sois jaune
    left(180)
    circle(50,360)#fais un cercle représentant le soleil
    end_fill()
    right(180) #redéfini l'angle à 0


def ciel():
    """
la fonction ciel() permet de faire un fond qui correspond à la  nuit
ou au jour, on appelera également la fonction lune ou soleil selon le cycle
"""
    n_j=randint(1,2)#donne chiffre 1ou2 au hasard qui ensuite va correspondre au jour ou la nuit
    if n_j==1:
        rectangle(0,-200,800,800,"cornflowerblue")#permet de faire un fond qui correspond au jour de couleur:cornflowerblue
        soleil()
    else:
        rectangle(0,-200,800,800,"darkblue")#permet de faire un fond qui correspond à la nuit de couleur:darkblue
        lune()
    return n_j

cycle=ciel()#pour les variables suivantes fenetres et lune_soleil sa va servir à garder le nombre au hasard choisis pour rester sur le thème jour et nuit en fonction du 1ou2 déjà choisis

def fenetre(x,y):
    """
la fonction fenetre(x,y) permet de tracer une fenêtre carré 
Elle à pour paramètre les coordonnées du milieu (x,y) de la base de la fenêtre
"""
    if cycle==1:
        rectangle(x,y,30,30,"white")#fait que des fenetres blanches en fonction du cycle près défini dans la fonction ciel() si il est égal à 1
    else:
        b=randint(1,2)#si cycle près défini dans la fonction ciel() est différent de 1 il va choisir un chiffre au hasard entre 1 et 2 qui va mettre que la fenetre sera jaune ou noir,sa correspond au fait qu'une lumière est allumé ou éteinte dans l'appartement sa va se répéter pour chaque fenetres
        if b==1:
            rectangle(x,y,30,30,"black")#si le chiffre choisis est 1 alors la fenetre sera noir
        else:
            rectangle(x,y,30,30,"yellow")#si le chiffre choisis est pas 1 alors la fenetre sera jaune

        
def etage(x,y,couleur):
    """
La fonction etage(x,y,couleur) permet de tracer un étage
Elle prend pour paramètre les coordonnées (x,y) du milieu de la base
de l'étag et la couleur qui définit la couleur de l'étage 
"""
    begin_fill()
    fillcolor(couleur)
    
    rectangle(x,y,160,60,couleur)#fait un rectangle qui est le mur de l'étage
    
    for i in range(3):
        fenetre(x-40,y+20)
        x=x+40#fait 3 carré sur le mur qui correspondent à des fenetres
    
    end_fill()
        
def porte(x,y,couleur):
    """
La fonction porte(x,y,couleur) permet de tracer une porte
Elle prend pour paramètre les coordonnées (x,y) du milieu de la base
de la porte et la couleur qui la définit 
"""
    couleur=couleur_aleatoire()
    begin_fill()
    fillcolor(couleur)
    
    rectangle(x,y,30,45,couleur)#fait un rectangle qui correspond à la porte
    
    end_fill()

def rdc(x,couleur):
    """
La fonction rdc(x,couleur) permet de tracer un rdc
Elle prend pour paramètre les coordonnées (x) du milieu de la base
du rdc et la couleur de remplissage qui la définit
"""
    position_porte=randint(0,2) #chiffre hasard 0,1 ou 2 qui servira à définir la postion de la porte
    begin_fill()
    fillcolor(couleur)
    
    rectangle(x,-200,160,60,couleur)#trace rectangle du rdc
    
    x=x-40#mets le crayon à l'abscisse ou sera fait sois la 1er fenetre ou la porte
    for i in range(3):
        if i==position_porte:#si position_porte est égal a i il fait une porte
            porte(x,-200,couleur)#si position_porte est pas égal a i il fait une fentres
        else:
            fenetre(x,-185)
        x=x+40#avance pour faire la prochaine fenetre ou la porte
    

def toit(x,y):
    """
La fonction toit(x,y) permet de tracer un toit
Elle prend pour paramètre les coordonnées (x,y) du milieu de la base
"""
    forme_toit=randint(1,3)
    
    if forme_toit==1:#si forme_toit est égal à 1 il sera en forme de triangle
        sommet_toit=randint(30,60)#définit le sommet du toit au hasard entre 30 et 60
        begin_fill()
        fillcolor("black")
        up()
        goto(x,y) #va au milieu de la base du toit
        down()
        
        forward(90) #va au sommet droit de l'immeuble
        goto(x,y+sommet_toit) #va au sommet du toit
        goto(x-90,y) #va au sommet gauche de l'immeuble
        forward(90) #on va replacer x au centre
        end_fill()
    
    if forme_toit==2:#si forme_toit est égal à 2 il sera en forme de rectangle
        begin_fill()
        fillcolor("black")
        up()
        goto(x,y) #va au milieu de la base du toit
        down()
        forward(85) #va un peu plus loin que le sommet droit de l'immeuble
        goto(x+85,y+15) #va au sommet droit du rectangle
        goto(x-85,y+15) #va au sommet gauche du rectangle
        goto(x-85,y) #va un peu plus loin que le sommet gauche de l'immeuble
        forward(85) #replace x au centre
        end_fill()
    
    if forme_toit==3: #si forme_toit est égal à 3 il sera en forme de trapèze
        z=randint(30,60)
        begin_fill()
        fillcolor("black")
        up()
        goto(x,y) #va au milieu de la base du toit
        down()
        forward(90) #se rend un plus loin que le sommet droit de l'immeuble
        goto(x+30,y+30) #va au sommet droit du trapèze 
        forward(-60) #va au sommet gauche du trapèze
        goto(x-90,y) #se rend un peu plus loin que le sommet gauche de l'immeuble
        forward(90) #replace x au centre
        end_fill()
        
def immeuble(x):
    """
La fonction immeuble(x) permet de tracer un immeuble
Elle prend pour paramètre les coordonnées (x) du milieu de la base
"""
    y=-140#chaque immeuble va commencé avec un ordonnée de -140
    couleur=couleur_aleatoire()
    n_etage=randint(0,4)#donne le nombre d'étage qui aura dans l'immeuble au hasard entre 0 et 4
    n_etagef=0
    
    rdc(x,couleur)#fait le rdc
    
    while n_etagef<n_etage:#fait une boucle qui temps n_etagef<n_etage il doit faire un autre étage et rajoute +1 à n_etagef
        n_etagef=n_etagef+1
        etage(x,y,couleur)
        y=y+60#augmente de 60 pixel l'ordonnée entre chaque étage
    
    toit(x,y)#fait le toit

def rue():
    """
La fonction rue() permet de tracer une rue 
"""
    x=-298 #abscisse du milieu du premier immeuble
    
    sol()#fait le sol
    route_herbes()#fait route_herbes
    
    for i in range(4):
        immeuble(x) #fait 4 immeubles
        x=x+190 #mets un écart de 190 pixels entre chaque milieux de base de chaque immeubles 
    up()
    goto(-10000,-10000) #enlève le stylo loin pour pas déranger
rue()
mainloop()
    
    
    
        

    
    
