# Factorielle

"""
Calcul de la factorielle d’un nombre
Écrivez une fonction récursive qui calcule la factorielle d’un entier positif n.
Par exemple : 5! = 5 × 4 × 3 × 2 × 1 = 120
"""

def factorielle(n):
    # base case
    if n == 0:
        return 1
    else:
        return n * factorielle(n-1)

print(factorielle(5)) # 120

#------------------------Exo 2---------------------------------------------#
"""
Somme des n premiers nombres
Écrivez une fonction récursive qui calcule la somme des nombres de 1 à n.
Par exemple :
somme(n)=n+(n−1)+⋯+1
"""

def somme(n):
    #base case
    if n==1:
        return 1
    #addition = n + n-1
    return n + somme(n-1)
n = 5
somme_prem = somme(n)
print(f"la somme de n premiers nombres de {n} est {somme_prem}")
#------------------------Exo 3---------------------------------------------#

"""
Compter les éléments d’une liste
Écrivez une fonction récursive qui compte le nombre d’éléments dans une liste.
"""
def count_liste(my_list:list):
    compteur = 0
    if len(my_list) == 0:
        return 0
    else:
        compteur += 1
        return compteur + count_liste(my_list[1:])
my_list = ["maman","papa",4,6,7,8,9]
nombre_element = count_liste(my_list)
print(f"le nombre d'éléments dans la liste est de: {nombre_element} ")










