inWord = input()
totalTime = 0

#걸리는 시간 = 번호 + 1
wordToNumDict = {
    "ABC" : 2,
    "DEF" : 3,
    "GHI" : 4,
    "JKL" : 5,
    "MNO" : 6,
    "PQRS" : 7,
    "TUV" : 8,
    "WXYZ" : 9
}

for i in inWord:
    for j in wordToNumDict:
        if i in j:
            totalTime += wordToNumDict[j] + 1

print(totalTime)