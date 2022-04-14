numOfCase = int(input())
sudokuList = []
checkList = [True for _ in range(numOfCase)]

# sudoku 입력
for i in range(numOfCase):
    sudoku = [list(map(int,input().split())) for _ in range(9)]
    if i != numOfCase-1:
        input()
    sudokuList.append(sudoku)

# 정답 확인
for i in range(numOfCase):
    # 행 검사
    for j in range(9):
        if sorted(sudokuList[i][j]) != [1,2,3,4,5,6,7,8,9]:
            checkList[i] = False
            break

    # 열 검사
    if checkList[i]:
        for j in range(9):
            columnsList = []
            for k in range(9):
                columnsList.append(sudokuList[i][k][j])
            if sorted(columnsList) != [1,2,3,4,5,6,7,8,9]:
                checkList[i] = False
                break

    # 3x3 검사
    if checkList[i]:
        tmp=[]
        for f in range(0,8,3):
            kCount = 0
            if not checkList[i]:
                break
            for j in range(3):
                jCount = f
                for k in range(3):
                    if kCount == 6:
                        tmp += sudokuList[i][jCount][kCount:]
                    else:
                        tmp += sudokuList[i][jCount][kCount:kCount + 3]
                    jCount += 1
                if sorted(tmp) != [1,2,3,4,5,6,7,8,9]:
                    print(tmp)
                    checkList[i] = False
                    break
                tmp = []
                kCount += 3

for i in range(numOfCase):
    if checkList[i]:
        print(f'Case {i + 1}: CORRECT')
    else:
        print(f'Case {i + 1}: INCORRECT')