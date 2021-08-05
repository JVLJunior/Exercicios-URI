n = int(input())
cont = 3
f1 = 0
f2 = 1
print('{} {}'.format(f1, f2), end='')
while cont <= n:
    f3 = f1 + f2
    print(' {}'.format(f3), end='')
    f1 = f2
    f2 = f3
    cont += 1
print('')
