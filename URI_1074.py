n = int(input())
i = 0
ns = []
while i < n:
    x = int(input())
    ns.append(x)
    i += 1
for a in range(len(ns)):
    if ns[a] == 0:
        print('NULL')
    elif ns[a] % 2 == 0:
        if ns[a] < 0:
            print('EVEN NEGATIVE')
        else:
            print('EVEN POSITIVE')
    else:
        if ns[a] < 0:
            print('ODD NEGATIVE')
        else:
            print('ODD POSITIVE')
