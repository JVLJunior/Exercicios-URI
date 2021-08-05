a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
hi = a * 60 + b
hf = c * 60 + d
if a < c:
    dr = hf - hi
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)' .format((dr - dr % 60) // 60, dr % 60))
elif a == c and b < d:
    print('O JOGO DUROU 0 HORA(S) E {} MINUTO(S)' .format(d - b))
elif a == c and b == d:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:
    dr = (hf + 1440) - hi
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)' .format(dr // 60, dr % 60))
