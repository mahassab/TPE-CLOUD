def somme_diviseurs_propres(n):
    """
    Calcule la somme des diviseurs propres d'un nombre `n`.
    Un diviseur propre est un diviseur strictement inférieur à `n`.
    """
    somme = 1  # 1 est un diviseur propre de tout nombre supérieur à 1
    for i in range(2, int(n**0.5) + 1):  # Parcourt les nombres jusqu'à la racine carrée de `n`
        if n % i == 0:  # Si `i` est un diviseur de `n`
            somme += i  # Ajoute le diviseur
            if i != n // i:  # Si `i` et `n // i` sont différents
                somme += n // i  # Ajoute également le diviseur complémentaire
    return somme  # Retourne la somme des diviseurs propres

def paires_amicales(deb, fin):
    """
    Trouve toutes les paires amicales dans la plage [deb, fin].
    Une paire (A, B) est amicale si :
      - La somme des diviseurs propres de A est égale à B.
      - La somme des diviseurs propres de B est égale à A.
    """
    paires = []  # Liste pour stocker les paires amicales
    calculs_diviseurs = {}  # Dictionnaire pour mémoriser les sommes des diviseurs propres

    # Calculer les sommes des diviseurs propres pour chaque nombre dans la plage
    for num in range(deb, fin + 1):
        calculs_diviseurs[num] = somme_diviseurs_propres(num)  # Stocke la somme des diviseurs propres

    # Vérifier chaque nombre pour identifier les paires amicales
    for a in range(deb, fin + 1):
        b = calculs_diviseurs[a]  # Récupère la somme des diviseurs propres de `a`
        if b > a and b <= fin and calculs_diviseurs.get(b) == a:  
            # Vérifie que :
            # 1. b > a (pour éviter les doublons)
            # 2. b est dans la plage [début, fin]
            # 3. La somme des diviseurs propres de `b` est égale à `a`
            paires.append((a, b))  # Ajoute la paire amicale (a, b) à la liste

    return paires  # Retourne toutes les paires amicales trouvées

# Tester le programme avec une plage 
deb =int(input("entrer la valeur du début :"));
fin =int (input ("entrer la valeur de la fin :")) # Plage des nombres à analyser
paires = paires_amicales(deb, fin)  # Trouve les paires amicales dans la plage
print("le(s) couple(s) parfait(s) dans cet intervalle sont : ")
print(paires)  # Affiche les paires amicales trouvées
