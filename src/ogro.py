E = int(input())
D = int(input())

if max(E, D) == E:
    print(E+D)
else:
    print(2*(D-E))