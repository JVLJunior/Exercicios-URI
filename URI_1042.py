a, b, c = input().split()
x = int(a)
y = int(b)
z = int(c)
if y > x < z:
    if y < z:
        x, y, z = x, y, z
    elif y > z:
        x, y, z = x, z, y
elif y > x > z:
    x, y, z = z, x, y
elif y < x < z:
    x, y, z = y, x, z
elif y < x > z:
    if y < z:
        x, y, z = y, z, x
    else:
        x, y, z = z, y, x
print('{} \n{} \n{}'.format(x, y, z))
print('')
print('{} \n{} \n{}'.format(a, b, c))
