dohaji=[[0 for _ in range(100)] for _ in range(100)]

colorPaperNum=int(input())
colorPaperIdxList=[list(map(int,input().split()))
                   for _ in range(colorPaperNum)]
result=0

for i in range(colorPaperNum):
    idx_x = colorPaperIdxList[i][1]
    idx_y = colorPaperIdxList[i][0]

    for j in range(idx_x-1,idx_x+9):
        for k in range(idx_y-1, idx_y+9):
            dohaji[j][k] = 1

for i in dohaji:
    result+=i.count(1)

print(result)