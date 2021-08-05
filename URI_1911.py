while True:
# criando o primeiro dicionário
    n = int(input())
    if n == 0:
        break
    alunos = {}
    i = 1
    while i <= n:
        a, b = input().split()
        alunos[a] = b
        i += 1
# criando o segundo dicionário
    presentes = {}
    m = int(input())
    j = 1
    while j <= m:
        c, d = input().split()
        presentes[c] = d
        j += 1
# Comparando os dicionários
    anome = []
    pnome = []
    dif = 0
    for k in presentes.keys():
        anome.clear()
        pnome.clear()
        if alunos[k] != presentes[k]:
            cont = 0
            for a in alunos[k]:
                anome.append(a)
            for p in presentes[k]:
                pnome.append(p)
            for l in range(len(anome)):
                if anome[l] != pnome[l]:
                    cont += 1
            if cont > 1:
                dif += 1
    print(dif)
