m = []
for n in range(0, 5):
    m.append(int(input()))
p = 0
i = 0
pp = 0
ng = 0
for c in range(len(m)):
    if m[c] % 2 == 0:
        p += 1
    else:
        i += 1
    if m[c] > 0:
        pp += 1
    elif m[c] < 0:
        ng += 1
print('{} valor(es) par(es)'.format(p))
print('{} valor(es) impar(es)'.format(i))
print('{} valor(es) positivo(s)'.format(pp))
print('{} valor(es) negativo(s)'.format(ng))
