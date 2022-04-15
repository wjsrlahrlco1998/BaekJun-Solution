from collections import deque

lenOfBelt, maxBrokenCount = map(int, input().split())
AList = list(map(int, input().split()))

# 벨트번호, 로봇유무, 내구도
Belt = [[i + 1, 0, AList[i]] for i in range(lenOfBelt * 2)]
Belt = deque(Belt)

# 진행단계
level = 0
# 내구성이 0인 칸의 개수
brokenCount = 0

def outRobot():
    if Belt[lenOfBelt - 1][1] == 1:
        Belt[lenOfBelt - 1][1] = 0

while maxBrokenCount > brokenCount:
    level += 1

    outRobot()

    # 1. 벨트회전
    Belt.rotate(1)

    outRobot()

    # 2. 로봇의 이동
    for i in range(lenOfBelt - 2, -1, -1):
        if Belt[i][1] == 1 and Belt[i + 1][1] == 0 and Belt[i + 1][2] >= 1:
            Belt[i][1] = 0
            Belt[i + 1][1] = 1
            Belt[i + 1][2] -= 1
            outRobot()
            if Belt[i+1][2] == 0:
                brokenCount += 1

    # 3. 로봇 올리기
    if Belt[0][2] != 0 and Belt[0][1] == 0:
        Belt[0][1] = 1
        Belt[0][2] -= 1
        if Belt[0][2] == 0:
            brokenCount += 1

print(level)