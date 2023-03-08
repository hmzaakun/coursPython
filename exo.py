# exo1
temps = 6.892
distance = 19.7
vitesse = distance / temps
print("La vitesse est:", vitesse, "m/s")


# exo2
nom = input("Entrez votre nom : ")
age = int(input("Entrez votre âge : "))
print("Vous vous appelez", nom, "et vous avez", age, "ans.")

# exo3
import math  
x = float(input("Entrez un nombre flottant : "))
if x >= 0:
    racine = math.sqrt(x)
    print("La racine carrée de", x, "est", racine)
else:
    print("Erreur : le nombre saisi est négatif.")


# exo4
mot1 = input("Entrez le premier mot : ")
mot2 = input("Entrez le deuxième mot : ")
if mot1 < mot2:
    print("Le mot", mot1, "vient avant", mot2, "dans l'ordre lexicographique.")
elif mot1 > mot2:
    print("Le mot", mot2, "vient avant", mot1, "dans l'ordre lexicographique.")
else:
    print("Les deux mots sont identiques.")


# exo5
pSeuil = 2.3
vSeuil = 7.41
pression = float(input("Entrez la pression courante de l'enceinte : "))
volume = float(input("Entrez le volume courant de l'enceinte : "))
if pression > pSeuil and volume > vSeuil:
    print("Arrêt immédiat : pression et volume trop élevés !")
elif pression > pSeuil:
    print("La pression est trop élevée. Augmentez le volume de l'enceinte.")
elif volume > vSeuil:
    print("Le volume est trop élevé. Diminuez le volume de l'enceinte.")
else:
    print("Tout va bien : pression et volume dans les limites autorisées.")


# exo6
chaine = input("Entrez une chaîne de caractères : ")
if '@' in chaine and chaine.endswith('.com'):
    print("C'est un email valide.")
else:
    print("Ce n'est pas un email valide.")


# exo7
message = input("Entrez le message à afficher : ")
for i in range(10):
    print("Ceci est le message numéro", i+1, ":", message)


# exo8
mot = input("Entrez un mot : ")
for lettre in mot:
    print(lettre)

# exo9
a = 0
b = 10
while a < b:
    print("a =", a)
    a += 1
while b != 0:
    b -= 1
    if b % 2 == 1:
        print("b =", b)


# exo10
while True:
    saisie = input("Saisir un entier entre 1 et 10 : ")
    try:
        entier = int(saisie)
    except ValueError:
        print("Erreur : saisie non valide.")
        continue
    if entier < 1 or entier > 10:
        print("Erreur : l'entier doit être entre 1 et 10.")
        continue
    break
print("Vous avez saisi :", entier)

# exo11
chaine = "Bonjour tout le monde !"
for caractere in chaine:
    print(caractere)
liste = [1, 2, 3, 4, 5]
for element in liste:
    print(element)
for i in range(0, 15, 3):
    print(i)

# exo12
n = int(input("Entrez un entier positif : "))
i = 0
compteur = 0
while compteur < n:
    if i % 2 == 0:
        print(i)
        compteur += 1
    i += 1

# exo13
n = int(input("Entrez un entier positif : "))
compteur = 0
for i in range(0, n*2, 2):
    if compteur < n:
        print(i)
        compteur += 1
    else:
        break


# exo15
liste = [17, 38, 10, 25, 72]
liste.sort()
print(liste)
liste.append(12)
print(liste)
liste.reverse()
print(liste)
print(liste.index(17))
liste.remove(38)
print(liste)
print(liste[1:3])
print(liste[:2])
print(liste[2:])
print(liste[:])

# exo16
chaine = input("Entrez une chaine de caractère à inverser : ")
print(chaine[::-1])

# exo17
chaine = input("Entrez une chaine qui est peut-être un palindrome : ")
if chaine == chaine[::-1]:
    print(chaine, "est un palindrome")


# exo18
chaine = input("Entrez un email valide ou non : ")
if '@' in chaine and '.' in chaine:
    partie_avant_point, partie_apres_point = chaine.rsplit(".", 1)
    if len(partie_apres_point) <= 3:
        print("La chaîne est un email valide")
    else:
        print("La chaîne n'est pas un email valide : trop de caractères après le point")
else:
    print("La chaîne n'est pas un email valide : pas de @")

    
# exo19
truc = []  
machin = [0.0] * 5  

print(truc) 
print(machin)  

# exo20
for i in range(4):
    print(i)
for i in range(4, 8):
    print(i)
for i in range(2, 9, 2):
    print(i)

#appartenance
chose = [0, 1, 2, 3, 4, 5]
print(3 in chose)  # affiche True
print(6 in chose)  # affiche False


# exo21
x = int(input("Entrez un nombre : "))

with open("data.txt", "w") as f:
    for i in range(x):
        chaine = input(f"Entrez la chaîne numéro {i+1} : ")
        f.write(chaine + "\n")

print("Les chaînes ont été enregistrées dans data.txt.")

# exo22
with open("data.txt", "r") as f:
    for line in f:
        line = line.strip()
        if "@" in line and line.endswith(".com"):
            print(f"{line} est un email.")
        else:
            print(f"{line} n'est pas un email.")

# exo23
def compterMots(chaine):
    chaine = chaine.lower()
    for c in [".", ",", ";", ":", "!", "?", "'"]:
        chaine = chaine.replace(c, " ")

    mots = chaine.split()
    freq = {}
    for mot in mots:
        if mot in freq:
            freq[mot] += 1
        else:
            freq[mot] = 1

    return freq


# exo24
def cube(x):
    return x * x * x

def volumeSphere(r):
    pi = 3.141592653589793
    v = (4 / 3) * pi * cube(r)
    return v


# exo25
def somme(a, b, c):
    return a + b + c
