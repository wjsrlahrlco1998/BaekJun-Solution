caseNum = int(input())
infoScoreList = []

for _ in range(caseNum):
    infoScoreList.append(list(map(int, input().split())))

for i in range(caseNum):
    scoreAverage=sum(infoScoreList[i][1:])/infoScoreList[i][0]
    upAverageNum=0
    for j in infoScoreList[i][1:]:
        if j > scoreAverage:
            upAverageNum+=1
    print(f'{upAverageNum/infoScoreList[i][0]*100:.3f}%')