fileNum=int(input())
fileNameList=[list(input()) for _ in range(fileNum)]
result=''

for i in range(len(fileNameList[0])):
    compareList=[]
    for j in range(fileNum):
        compareList.append(fileNameList[j][i])
    if compareList.count(compareList[0]) == fileNum:
        result+=compareList[0]
    else:
        result+='?'
print(result)