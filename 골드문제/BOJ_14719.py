H, W = map(int, input().split())
block = list(map(int, input().split()))

plainWorld = [[0 for _ in range(W)] for _ in range(H)]
rainTotalCount = 0

for i in range(W):
    for j in range(H):
        if block[i] > j:
            plainWorld[j][i] = '='

for i in range(H):
    rainCount = 0
    start = -1
    end = -1
    for j in range(W):
        if plainWorld[i][j] == '=' and start == -1:
            start = 1
        elif start == 1 and plainWorld[i][j] == 0:
            rainCount += 1
            end = 0
        elif start == 1 and end == 0 and plainWorld[i][j] == '=':
            end = 1

        if end == 1:
            rainTotalCount += rainCount
            end = -1
            rainCount = 0

print(rainTotalCount)

