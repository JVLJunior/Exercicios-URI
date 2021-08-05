n = int(input())
i = 0
o = 0
for a in range(1, n + 1):
    x = int(input())
    if 10 <= x <= 20:
        i = i + 1
    else:
        o = o + 1
print('{} in'.format(i))
print('{} out'.format(o))
