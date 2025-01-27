# Exo 1
"""
Recherche d’un élément dans une liste
Écrivez une fonction récursive qui vérifie si un élément x est présent dans une liste.
"""
def searching(my_list,value):
    #cas de base
    if len(my_list) == 0:
        return None

    if my_list[0] == value:
        return True
    else:
        return searching(my_list[1:],value)


#print(searching([4,6,7,9,9,7,'X'],'X'))

# Exo 2

"""
Inversement d’une chaîne de caractères
Écrivez une fonction récursive qui inverse une chaîne de caractères.
"""
def uno_reverse(my_string):
    #reverse_string = ""
    if len(my_string) == 0:
        return ""

    return my_string[-1] + uno_reverse(my_string[:-1])

my_string = "je"
print(uno_reverse(my_string))



