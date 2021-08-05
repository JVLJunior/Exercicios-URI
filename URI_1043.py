t = []
a, b, c = input().split()
t.append(float(a))
t.append(float(b))
t.append(float(c))
t = sorted(t, reverse=True)
if t[0] >= t[1] + t[2]:
    print('Area = {}'.format(((t[0] + t[1]) / 2) * t[2]))
else:
    print('Perimetro = {}'.format(t[0] + t[1] + t[2]))
