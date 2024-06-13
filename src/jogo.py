neighs = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    ]



pl = input().split(" ")
N, Q = int(pl[0]), int(pl[1])

MORTA = 0
VIVA = 1

def in_m(i: int, j: int, n: int) -> bool:
    if i >= N:
        return False
    if j >= N:
        return False
    if j < 0:
        return False
    if i < 0:
        return False
    return True
    

def count_neigh_vivo(i: int, j: int, m: list[list[int]]) -> int:
    live_count = 0
    for pos in neighs:
        ni = i+pos[0]
        nj = j+pos[1]
        if in_m(ni, nj, N):
            live_count += m[ni][nj]

    return live_count

def print_state(state):
    for row in state:
        for cell in row:
            print(cell, end="")
        print()
def print_state_funny(state):
    for i,  row in enumerate(state):
        for j, cell in enumerate(row):
            print(count_neigh_vivo(i, j, state), end="")
        print()

state = [[0 for _ in range(N)] for _ in range(N)]
next_state = [[0 for _ in range(N)] for _ in range(N)]

i = 0
while i < N:
    line = input()
    for j, c in enumerate(line):
        state[i][j] = int(c)
    i += 1

# print_state(state)
# print()
# print()
# print_state_funny(state)



# print()
# print_state(state)
# print()
for _ in range(Q):
    for i, row in enumerate(state):
        for j, cell in enumerate(row):
            if cell == MORTA:
                if count_neigh_vivo(i, j, state) == 3:
                    next_state[i][j] = VIVA
            elif cell == VIVA:
                ngs = count_neigh_vivo(i, j, state)
                if ngs == 2 or ngs == 3:
                    next_state[i][j] = VIVA 
                else:
                    next_state[i][j] = MORTA 
    state = [[cell for cell in row] for row in next_state]

print_state(state)