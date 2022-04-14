numOfCase = int(input())
sudokuList = []
checkList = [True for _ in range(numOfCase)]

# sudoku 입력
for i in range(numOfCase):
    sudoku = [list(map(int,input().split())) for _ in range(9)]
    if i != numOfCase-1:
        input()
    sudokuList.append(sudoku)
tmp = []
jCount = 0
kCount = 0
for i in range(numOfCase):
    for f in range(0,8,3):
        kCount = 0
        for j in range(3):
            jCount = f
            print(f)
            for k in range(3):
                if kCount == 6:
                    print(*sudokuList[i][jCount][kCount:])
                    tmp += sudokuList[i][jCount][kCount:]
                else:
                    print(*sudokuList[i][jCount][kCount:kCount + 3])
                    tmp += sudokuList[i][jCount][kCount:kCount + 3]
                jCount += 1
            print('-'*20)
            print(sorted(tmp))
            tmp=[]
            kCount += 3
for i in range(numOfCase):
    for j in sudokuList[i]:
        print(*j)
