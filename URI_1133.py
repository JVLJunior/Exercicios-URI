x = int(input())
y = int(input())
if x <= y:
    a = x
    b = y
else:
    a = y
    b = x
for n in range(a + 1, b):
    if (n % 5 == 2) or (n % 5 == 3):
        print(n)
