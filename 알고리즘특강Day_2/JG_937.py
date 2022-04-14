firstList=[[_ for _ in range(3)] for _ in range(2)]
secondList=[[_ for _ in range(3)] for _ in range(2)]
resultList=[[_ for _ in range(3)] for _ in range(2)]

for i in range(2):
    if i == 0:
        print('(출력)first array')
        firstList[0] = list(map(int, input().split()))
        firstList[1] = list(map(int, input().split()))
    else:
        print('(출력)second array')
        secondList[0] = list(map(int, input().split()))
        secondList[1] = list(map(int, input().split()))

for i in range(2):
    for j in range(3):
        resultList[i][j] = firstList[i][j]*secondList[i][j]

for i in range(2):
    for j in range(3):
        print(f'{resultList[i][j]}',end=' ')
    print()