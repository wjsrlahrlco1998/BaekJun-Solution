groupCount, quizCount = map(int, input().split())
groupDict = {}
quizDict = {}

for _ in range(groupCount):
    groupName = input()
    groupDict[groupName] = []
    groupMemberCount = int(input())
    for _ in range(groupMemberCount):
        groupDict[groupName].append(input())

for _ in range(quizCount):
    quizName = input()
    quizType = int(input())
    quizDict[quizName] = quizType

for quizName, quizType in quizDict.items():
    if quizType == 0:
        print(*sorted(groupDict[quizName]), sep='\n')
    else:
        for gName in groupDict:
            if quizName in groupDict[gName]:
                print(gName)