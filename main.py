"""
Module pour encoder une chaîne de caractères en une liste de tuples
indiquant chaque caractère et son nombre d'occurrences consécutives.
"""
import sys

def artcode_i(s):
    """
    Retourne la liste de tuples encodant une chaîne de caractères
    passée en argument selon un algorithme itératif.

    Args:
        s (str): la chaîne de caractères à encoder.

    Returns:
        list: liste de tuples (caractère, nombre d'occurrences).
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
    """
    Retourne la liste de tuples encodant une chaîne de caractères
    passée en argument selon un algorithme récursif.

    Args:
        s (str): la chaîne de caractères à encoder.

    Returns:
        list: liste de tuples (caractère, nombre d'occurrences).
    """
    if len(s) == 0:
        return []

    index = 1
    while index < len(s) and s[0] == s[index]:
        index += 1

    # Appel récursif sur la sous-chaîne restante
    return [(s[0], index)] + artcode_r(s[index:])


def main():
    """
    Fonction principale pour tester les encodages itératif et récursif.
    """
    # Augmenter raisonnablement la limite de récursion
    sys.setrecursionlimit(1100)

    chaine = "MMMMaaacXo\nlloMM"

    print("Encodage itératif :", artcode_i(chaine))
    print("Encodage récursif :", artcode_r(chaine))


if __name__ == "__main__":
    main()
