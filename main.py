#### Imports et définition des variables globales

import sys

#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    tab = []
    index_d = 0
    while index_d < len(s):
        index = index_d
        compteur = 0
        while index < len(s) and s[index_d] == s[index]:
            compteur += 1
            index += 1
        tab.append((s[index_d], compteur))
        index_d = index
    return tab


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    
    # votre code ici

    # cas de base
    # recherche nombre de caractères identiques au premier
    # appel récursif
    #tab = []
    if len(s) == 0: return[];
    compteur = 1
    index = 1
    while index < len(s) and s[0] == s[index]:
        compteur += 1
        index += 1
    return [(s[0],compteur)] + artcode_r(s[index:])

#### Fonction principale


def main():
    sys.setrecursionlimit(10**9)
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
