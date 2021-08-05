i = int(input())
print('{} ano(s)'.format(i // 365))
print('{} mes(es)'.format((i % 365) // 30))
print('{} dia(s)'.format((i % 365) % 30))
