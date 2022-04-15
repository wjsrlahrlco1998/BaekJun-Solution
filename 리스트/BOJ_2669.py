plane = [[0 for _ in range(100)] for _ in range(100)]
squareList = [list(map(int,input().split())) for _ in range(4)]
result=0

for i in range(4):
    start_x = squareList[i][1]
    start_y = squareList[i][0]
    end_x = squareList[i][3]
    end_y = squareList[i][2]

    for j in range(start_x, end_x):
        for k in range(start_y, end_y):
            plane[j][k]=1

for i in plane:
    result+=i.count(1)

print(result)