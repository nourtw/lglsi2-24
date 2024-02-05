def carre(nombre):
    return nombre ** 2
    #corrected 'retourner' to 'return'
def somme_carres_pairs(n):
    somme = 0
    for i in range(n):  # corrected 'pour' to 'for' and 'plage' to 'range'
        if i % 2 == 0:   # corrected 'si' to 'if' and '= 0' to '== 0'
            somme += carre(i)
        else:
            somme += i
    return somme

n = 10
resultat = somme_carres_pairs(n)
print("La somme des carrés des nombres pairs jusqu'à", n, "est :", resultat)  # corrected 'imprimer' to 'print'
