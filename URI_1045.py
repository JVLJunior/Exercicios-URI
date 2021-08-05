t = []
a, b, c = input().split()
t.append(float(a))
t.append(float(b))
t.append(float(c))
t = sorted(t, reverse=True)
if t[0] >= t[1] + t[2]:
    print('NAO FORMA TRIANGULO')
else:
    if (t[0] ** 2 == t[1] ** 2 + t[2] ** 2):
        print("TRIANGULO RETANGULO")
    if (t[0] ** 2 > t[1] ** 2 + t[2] ** 2):
        print("TRIANGULO OBTUSANGULO")
    if (t[0] ** 2 < t[1] ** 2 + t[2] ** 2):
        print("TRIANGULO ACUTANGULO")
    if (t[0] == t[1] == t[2]):
        print("TRIANGULO EQUILATERO")
    elif (t[0] == t[1]):
        print("TRIANGULO ISOSCELES")
    elif (t[0] == t[2]):
        print("TRIANGULO ISOSCELES")
    elif (t[1] == t[2]):
        print("TRIANGULO ISOSCELES")
