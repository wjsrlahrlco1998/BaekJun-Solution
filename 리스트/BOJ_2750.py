numOfLine=int(input())
numList=[]
for _ in range(numOfLine):
    numList.append(int(input()))

numList=sorted(numList)

for i in numList:
    print(i)