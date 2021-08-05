nt = []
while len(nt) < 2:
    n = float(input())
    if 0 <= n <= 10:
        nt.append(n)
    else:
        print('nota invalida')

print('media = {}'.format((nt[0] + nt[1]) / 2))
