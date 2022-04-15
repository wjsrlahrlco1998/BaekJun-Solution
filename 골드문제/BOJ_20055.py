import time

lenOfBelt, maxBrokenCount = map(int, input().split())
AList = list(map(int, input().split()))

Belt = [[i + 1, 0, 0] for i in range(lenOfBelt * 2)]

level = 0
brokenCount = 0

for i in range(lenOfBelt * 2):
    Belt[i][2] = AList[i]

while maxBrokenCount > brokenCount:
    level += 1
    brokenCount = 0
    print(level,Belt)

    # 1. 벨트회전
    Belt.insert(0, Belt[-1])
    del Belt[-1]
    # 로봇 내리기
    if Belt[lenOfBelt - 1][1] == 1:
        Belt[lenOfBelt - 1][1] = 0
    print(level,Belt)

    # 2. 로봇의 이동
    yesMove = []
    for i in range(lenOfBelt - 2, -1, -1):
        if Belt[i][1] == 1 and Belt[i + 1][1] == 0 and Belt[i + 1][2] >= 1:
            yesMove.append(i)
    for i in yesMove:
        Belt[i][1] = 0
        Belt[i+1][1] = 1
        Belt[i+1][2] -= 1
        # 로봇 내리기
        if Belt[lenOfBelt - 1][1] == 1:
            Belt[lenOfBelt - 1][1] = 0
    print(level,Belt)

    # 3. 로봇 올리기
    if Belt[0][2] != 0 and Belt[0][1] == 0:
        Belt[0][1] = 1
        Belt[0][2] -= 1
    print(level, Belt)

    # 4. brokenCount 검사
    for i in range(lenOfBelt * 2):
        if Belt[i][2] == 0:
            brokenCount += 1
    print('='*70)
    #time.sleep(1)
print(level)
print(brokenCount)