def ma_moyenne_listes(*listes):
    somme = 0
    longueur = 0
    for liste in listes:
        somme += sum(liste)
        longueur += len(liste)
    return somme / longueur



def python_in_str(chaine_python):
    """ Cette fonction renvoie bravo! si le mot
    python est compris dans la chaine de caractère"""
    if "python" in chaine_python:
        return "bravo !"
    else:
        return "autre"
