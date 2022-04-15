numList=list(map(int, input().split()))
result=False

while not result:
    if numList[0] > numList[1]:
        tmp = numList[0]
        numList[0] = numList[1]
        numList[1] = tmp
        print(*numList)

    if numList[1] > numList[2]:
        tmp = numList[1]
        numList[1] = numList[2]
        numList[2] = tmp
        print(*numList)

    if numList[2] > numList[3]:
        tmp = numList[2]
        numList[2] = numList[3]
        numList[3] = tmp
        print(*numList)

    if numList[3] > numList[4]:
        tmp = numList[3]
        numList[3] = numList[4]
        numList[4] = tmp
        print(*numList)

    if numList == [1,2,3,4,5]:
        result = True