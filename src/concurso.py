K = int(input().split(" ")[1])

notas = reversed(sorted([int(n) for n in input().split(" ")]))
aprovado = 0

for n in notas:
    aprovado += 1

    if aprovado == K:
        print(n)
        exit()
