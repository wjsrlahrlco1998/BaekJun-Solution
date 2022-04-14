# n은 홀수
n = int(input())
findNum = int(input())

snail = [[0 for _ in range(n)] for _ in range(n)]

start = n//2
x = start
y = start
signX = [0,1,0,-1]
signY = [1,0,-1,0]
idx = 0

walk = 0
weight = 1
changeCount = 0

for i in range(1, n*n+1):

    if walk == 1 * weight:
        idx = (idx + 1) % 4
        walk = 0
        changeCount += 1

    snail[y][x] = i
    if snail[y][x] == findNum:
        find_x = n - y
        find_y = x + 1

    x += signX[idx]
    y += signY[idx]

    if changeCount == 2:
        changeCount = 0
        weight += 1

    walk += 1

for i in snail[::-1]:
    print(*i, sep=' ')
print(find_x, find_y)
