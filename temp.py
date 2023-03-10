import tkinter as tk

class AB:
    def __init__(self, racine=None, gauche=None, droite=None):
        self.racine = [racine]
        self.gauche = gauche
        self.droite = droite
    
    def set_racine(self, valeur):
        self.racine = [valeur]
        
    def set_gauche(self, ab):
        self.gauche = ab
        
    def set_droite(self, ab):
        self.droite = ab

    def estVide(self):
        if self is None:
            return True
        else:
            return self.racine == [None] and self.gauche is None and self.droite is None


    
    def taille(self):
        if self.estVide():
            return 0
        else:
            return 1 + (self.gauche.taille() if self.gauche is not None else 0) + (self.droite.taille() if self.droite is not None else 0)
        
    def prefixe(self):
        if not self.estVide():
            print(self.racine)
            if self.gauche is not None:
                self.gauche.prefixe()
            if self.droite is not None:
                self.droite.prefixe()

    def postfixe(self):
        if not self.estVide():
            if self.gauche is not None:
                self.gauche.postfixe()
            if self.droite is not None:
                self.droite.postfixe()
            print(self.racine)

    def infixe(self):
        if not self.estVide():
            if self.gauche is not None:
                self.gauche.infixe()
            print(self.racine)
            if self.droite is not None:
                self.droite.infixe()
    
    def hauteur(self):
        if self.estVide():
            return -1
        else:
            return 1 + max(self.gauche.hauteur() if self.gauche is not None else -1,
                           self.droite.hauteur() if self.droite is not None else -1)
        
    def estABR(self):
        if self.estVide():
            return True
        elif self.gauche is None and self.droite is None:
            return True
        elif self.gauche is None:
            return self.droite.racine > self.racine and self.droite.estABR()
        elif self.droite is None:
            return self.gauche.racine < self.racine and self.gauche.estABR()
        else:
            return self.gauche.racine < self.racine < self.droite.racine and self.gauche.estABR() and self.droite.estABR()
        
def arbreTxt(nom_fichier):
    with open(nom_fichier, 'r') as f:
        ligne = f.readline()
        return eval(ligne)

AbTxt = arbreTxt("arbre.txt")
print("\ninfixe de AbTxt :")
AbTxt.infixe()

        
arbre = AB(2)
arbre.set_gauche(AB(1))
arbre.set_droite(AB(3))
print("arbre a une taille de :" ,arbre.taille())        

A1 = AB(1)
print("a1 est il vide :" ,A1.estVide())
print("a1 a une taille de :" ,A1.taille())
        
A4 = AB(4)
A5 = AB(5)
A6 = AB(6)
A7 = AB(7, AB(7,AB(),AB(8,AB(1,AB(2)))))
A2 = AB(2, A4, A5)
A3 = AB(3, A6, A7)
Atest2 = AB(1, A2, A3)

Atest = AB(10,
        AB(5, AB(3), AB(8)),
        AB(12))

print("\nAtest a une hauteur de :" ,Atest.hauteur())

print("\npostfixe de Atest :")
Atest.postfixe()

print("\nprefixe de Atest :")
Atest.prefixe()

print("\ninfixe de Atest :")
Atest.infixe()

print("\nAtest est ABR :" ,Atest.estABR())




def dessinerAB(ab, canvas, x, y, dx):
    if ab is not None:
        # Dessin de la racine
        canvas.create_oval(x-15, y-15, x+15, y+15, fill='lightblue', outline='black')
        canvas.create_text(x, y, text=str(ab.racine[0]))
        
        #branche gauche
        if ab.gauche is not None:
            x_gauche = x - dx
            y_gauche = y + 50
            canvas.create_line(x, y, x_gauche, y_gauche, arrow='last')
            dessinerAB(ab.gauche, canvas, x_gauche, y_gauche, dx/2)
        
        #branche droite
        if ab.droite is not None:
            x_droite = x + dx
            y_droite = y + 50
            canvas.create_line(x, y, x_droite, y_droite, arrow='last')
            dessinerAB(ab.droite, canvas, x_droite, y_droite, dx/2)

#fenêtre
root = tk.Tk()
root.title("Affichage de l'arbre Atest")

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

dessinerAB(AbTxt, canvas, 400, 50, 200)

root.mainloop()