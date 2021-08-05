v1 = int(input())
v2 = int(input())
if v1 > v2:
    a = v2
    b = v1
else:
    a = v1
    b = v2
a += 1
s = 0
for n in range(a, b):
    if n % 2 != 0:
        s += n
print(s)
